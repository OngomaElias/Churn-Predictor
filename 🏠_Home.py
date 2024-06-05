import streamlit as st

st.title("Churn Predictor!")

name = st.text_input('What is your name?')

st.write(f'Hello, {name}')