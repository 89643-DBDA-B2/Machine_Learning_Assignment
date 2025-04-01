import streamlit as st
import pickle
import pandas as pd

with open("D:/temporary/Machine_Learning/assignment1/insurance_predictor_model.pkl" , "rb") as file:
    model = pickle.load(file)

st.header("Welcome to Insurance predictor model")
st.subheader("Predict insurance using age")

age = st.number_input("Enter your age here")

if st.button("Predict"):
    predict_df = pd.DataFrame({
        "age": age,
    }, index=["age"])

    predictions = model.predict(predict_df)

    st.write(f"Insurance will be {predictions[0]}")