import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("model.pkl")

# Title
st.title("💸 Dowry Predictor ")
st.caption("Made by Vaibhav Bhardwaj. Powered by sarcasm. 🐍")

# Form UI
gender = st.selectbox("👫 Gender", ["Male", "Female"])
education = st.selectbox("🎓 Education Level", ["School", "Graduate", "Postgraduate"])
income = st.selectbox("💰 Income Level", ["Low", "Middle", "High"])
location = st.selectbox("📍 Location", ["Urban", "Rural"])
profession = st.selectbox("🧑‍💼 Profession", [
    "Software Engineer", "Doctor", "Government Officer", "Teacher", "Business Owner", "Farmer"
])

# Predict button
if st.button("💍 Predict Dowry Amount"):
    input_df = pd.DataFrame([{
        "Gender": gender,
        "Education_Level": education,
        "Income_Level": income,
        "Urban_Rural": location,
        "Profession": profession
    }])

    result = model.predict(input_df)[0]
    st.success(f"🤑 Expected Dowry: ₹ {round(result, 2)} Lakhs")
    st.markdown("> \"Aaj ka gyaan.-from VAIBHAV BHARDWAJ\"")
    st.markdown("> \"Dowry is not a tradition — it’s a gift from the family so accept it hapily .\"")

