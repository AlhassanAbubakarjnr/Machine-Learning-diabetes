# ============================================
# Simple Streamlit App: Diabetes Prediction
# ML Model: Logistic Regression
# ============================================

import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# App title
st.title("🩺 Diabetes Prediction App")
st.write("A simple Machine Learning app using Logistic Regression")

# Load dataset
data = pd.read_csv("diabetes.csv")

# Split features and target
X = data.drop("Outcome", axis=1)
y = data["Outcome"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Sidebar inputs
st.sidebar.header("Enter Patient Data")

def user_input():
    pregnancies = st.sidebar.number_input("Pregnancies", 0, 20, 1)
    glucose = st.sidebar.number_input("Glucose", 0, 200, 120)
    blood_pressure = st.sidebar.number_input("Blood Pressure", 0, 140, 70)
    skin_thickness = st.sidebar.number_input("Skin Thickness", 0, 100, 20)
    insulin = st.sidebar.number_input("Insulin", 0, 900, 80)
    bmi = st.sidebar.number_input("BMI", 0.0, 70.0, 25.0)
    dpf = st.sidebar.number_input("Diabetes Pedigree Function", 0.0, 3.0, 0.5)
    age = st.sidebar.number_input("Age", 1, 120, 30)

    return pd.DataFrame({
        "Pregnancies": [pregnancies],
        "Glucose": [glucose],
        "BloodPressure": [blood_pressure],
        "SkinThickness": [skin_thickness],
        "Insulin": [insulin],
        "BMI": [bmi],
        "DiabetesPedigreeFunction": [dpf],
        "Age": [age]
    })

# Get user input
input_data = user_input()

# Display input
st.subheader("Patient Input Data")
st.write(input_data)

# Prediction
prediction = model.predict(input_data)

# Output
st.subheader("Prediction Result")

if prediction[0] == 1:
    st.error("⚠️ The model predicts: Diabetic")
else:
    st.success("✅ The model predicts: Not Diabetic")
