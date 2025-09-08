import streamlit as st
import joblib

model = joblib.load("regression.joblib")
size = st.number_input("size")
bedrooms = st.number_input("number of bedrooms")
garden = st.number_input("has a garden")

prediction = model.predict([[size, bedrooms, garden]])
st.write(f"The predicted price is {prediction[0]}")