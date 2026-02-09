import streamlit as st
import tensorflow as tf
import numpy as np

st.set_page_config(page_title="Customer Churn Prediction", page_icon="💡", layout="centered")

# TensorFlow version check
st.write("TensorFlow version:", tf.__version__)

st.title("💡 Customer Churn Prediction App")

# Sidebar for user input
st.sidebar.header("Enter Customer Details")

geography = st.sidebar.selectbox("Geography", ["France", "Spain", "Germany"])
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
age = st.sidebar.slider("Age", 18, 100, 30)
balance = st.sidebar.number_input("Balance", min_value=0.0, max_value=10000000.0, value=0.0)
credit_score = st.sidebar.number_input("Credit Score", min_value=0.0, max_value=1.0, value=0.0)
estimated_salary = st.sidebar.number_input("Estimated Salary", min_value=0.0, max_value=10000000.0, value=0.0)
tenure = st.sidebar.slider("Tenure (years)", 0, 10, 0)
num_products = st.sidebar.slider("Number of Products", 1, 4, 1)
has_credit_card = st.sidebar.selectbox("Has Credit Card?", ["No", "Yes"])
is_active_member = st.sidebar.selectbox("Is Active Member?", ["No", "Yes"])

# Encoding categorical variables
geo_map = {"France": 0, "Spain": 1, "Germany": 2}
gender_map = {"Male": 0, "Female": 1}
yes_no_map = {"No": 0, "Yes": 1}

input_data = np.array([[
    geo_map[geography],
    gender_map[gender],
    age,
    credit_score,
    balance,
    estimated_salary,
    tenure,
    num_products,
    yes_no_map[has_credit_card],
    yes_no_map[is_active_member]
]], dtype=float)

st.write("Input Data:", input_data)

# Dummy model for demo (replace with your trained model)
# Here we just calculate a fake probability
def dummy_model(x):
    # Simple formula for demo
    prob = 0.1*x[0,2]/100 + 0.2*x[0,4]/1000000 + 0.1*x[0,5]/1000000
    return min(prob, 1.0)

if st.button("Predict Churn Probability"):
    probability = dummy_model(input_data)
    st.success(f"Predicted Churn Probability: {probability*100:.2f}%")
