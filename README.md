# 🏡 Bangalore House Price Predictor

A machine learning-based web application that predicts residential property prices in Bangalore based on square footage, number of bathrooms, BHK (bedrooms), and specific location features. Developed as a personal portfolio project for showcasing practical data science and deployment skills.

---

## 🚀 Features
* **Data Cleaning & Preprocessing:** Handles missing values, standardizes square footage ranges (e.g., converting ranges into exact averages), and extracts features like BHK from raw text data.
* **Machine Learning Model:** Built using **Scikit-learn** (`LinearRegression`) with One-Hot Encoded locations for enhanced prediction accuracy.
* **Interactive User Interface:** A clean, responsive web app built with **Streamlit** where users can input house dimensions via sliders and select locations from a dropdown menu for instant price estimation.
* **Model Persistence:** Uses **Joblib** to save and load the trained model and column structure efficiently.

---

## 🛠️ Tech Stack & Libraries
* **Python**
* **Pandas & NumPy** (Data manipulation & cleaning)
* **Scikit-learn** (Machine Learning model & metrics)
* **Joblib** (Model serialization)
* **Streamlit** (Web application UI)

---

## 📂 Project Structure
```text
├── app.py                     # Streamlit web application script
├── bangalore_house_model.pkl  # Trained Linear Regression model
├── model_columns.pkl          # Saved list of model training columns
├── housing.csv                # Bengaluru house pricing dataset
└── requirements.txt           # Project dependencies
