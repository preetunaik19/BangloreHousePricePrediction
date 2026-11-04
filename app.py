import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the saved model and column structure
model = joblib.load('bangalore_house_model.pkl')
model_columns = joblib.load('model_columns.pkl')

st.title("🏡 Bangalore House Price Predictor")
st.write("Developed by **Preetam M Naik** | PES University")
st.markdown("---")

# User Input Controls
col1, col2 = st.columns(2)

with col1:
    sqft = st.number_input('Total Square Feet', min_value=300, max_value=15000, value=1200)
    bath = st.slider('Number of Bathrooms', min_value=1, max_value=6, value=2)

with col2:
    bhk = st.slider('BHK (Bedrooms)', min_value=1, max_value=6, value=2)
    
    # Extract location names from saved model columns
    location_cols = [col.replace('location_', '') for col in model_columns if col.startswith('location_')]
    selected_location = st.selectbox('Select Location', location_cols)

# Predict Button
if st.button('Predict Price', type='primary'):
    # Create an input dataframe filled with 0s matching the trained model's columns
    input_data = pd.DataFrame(columns=model_columns)
    input_data.loc[0] = 0 

    # Assign user inputs
    input_data['total_sqft'] = sqft
    input_data['bath'] = bath
    input_data['bhk'] = bhk

    # Activate the selected location column
    loc_column_name = f'location_{selected_location}'
    if loc_column_name in input_data.columns:
        input_data[loc_column_name] = 1

    # Make Prediction
    prediction = model.predict(input_data)[0]
    
    st.success(f"### Estimated Property Price: ₹ {prediction:,.2f} Lakhs")
