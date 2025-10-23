import streamlit as st
import numpy as np
import pickle

# Load the model
with open("diabetes_model.pkl", "rb") as f:
    model = pickle.load(f)
print(type(model))
# Title
st.title("Diabetes Prediction UI")

# User Inputs
pregnancies = st.number_input("Pregnancies", 0, 20)
glucose = st.number_input("Glucose", 0, 200)
bp = st.number_input("Blood Pressure", 0, 150)
skin = st.number_input("Skin Thickness", 0, 100)
insulin = st.number_input("Insulin", 0, 1000)
bmi = st.number_input("BMI", 0.0, 70.0)
dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0)
age = st.number_input("Age", 10, 100)

# Predict Button
if st.button("Predict"):
    input_data = np.array([[pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]])
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][prediction]

    if prediction == 1:
        st.success(f"Survived and probability {probability:2f}")
    else:
        st.error(f"Not Survived and probability {probability:2f}")