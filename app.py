import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model, scaler and feature columns
model = joblib.load("models/fraud_detection_model.pkl")
scaler = joblib.load("models/fraud_scaler.pkl")
feature_columns = joblib.load("models/feature_columns.pkl")

st.title("💳 Credit Card Fraud Detection System")

st.write("Enter transaction details below:")

amt = st.number_input("Transaction Amount", min_value=0.0)
gender = st.selectbox("Gender", ["Male", "Female"])
gender = 1 if gender == "Male" else 0
city_pop = st.number_input("City Population", min_value=0)
unix_time = st.number_input("Unix Time", min_value=0)
lat = st.number_input("Customer Latitude")
long = st.number_input("Customer Longitude")
merch_lat = st.number_input("Merchant Latitude")
merch_long = st.number_input("Merchant Longitude")

if st.button("Predict Fraud"):

    # Create empty dataframe with all training columns
    input_df = pd.DataFrame(np.zeros((1, len(feature_columns))), columns=feature_columns)

    # Fill known numeric features
    if 'amt' in input_df.columns:
        input_df['amt'] = amt
    if 'gender' in input_df.columns:
        input_df['gender'] = gender
    if 'city_pop' in input_df.columns:
        input_df['city_pop'] = city_pop
    if 'unix_time' in input_df.columns:
        input_df['unix_time'] = unix_time
    if 'lat' in input_df.columns:
        input_df['lat'] = lat
    if 'long' in input_df.columns:
        input_df['long'] = long
    if 'merch_lat' in input_df.columns:
        input_df['merch_lat'] = merch_lat
    if 'merch_long' in input_df.columns:
        input_df['merch_long'] = merch_long

    # Scale
    input_scaled = scaler.transform(input_df)

    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.error("⚠ Fraud Transaction Detected")
    else:
        st.success("✅ Legitimate Transaction")