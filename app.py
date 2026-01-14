import streamlit as st
import pandas as pd
import joblib

# Load trained pipeline
model = joblib.load("student_score_model.pkl")

st.set_page_config(page_title="Student Score Prediction", layout="centered")

st.title("🎓 Student Math Score Prediction")
st.write("Predict a student's math score using academic and demographic information.")

# User inputs
gender = st.selectbox("Gender", ["female", "male"])
race = st.selectbox(
    "Race/Ethnicity",
    ["group A", "group B", "group C", "group D", "group E"]
)
parent_edu = st.selectbox(
    "Parental Level of Education",
    [
        "some high school",
        "high school",
        "some college",
        "associate's degree",
        "bachelor's degree",
        "master's degree"
    ]
)
lunch = st.selectbox("Lunch Type", ["standard", "free/reduced"])
test_prep = st.selectbox("Test Preparation Course", ["none", "completed"])

reading_score = st.slider("Reading Score", 0, 100, 70)
writing_score = st.slider("Writing Score", 0, 100, 70)

# Prediction button
if st.button("Predict Math Score"):
    input_data = pd.DataFrame({
        "gender": [gender],
        "race/ethnicity": [race],
        "parental level of education": [parent_edu],
        "lunch": [lunch],
        "test preparation course": [test_prep],
        "reading score": [reading_score],
        "writing score": [writing_score]
    })

    prediction = model.predict(input_data)[0]

    st.success(f"📊 Predicted Math Score: **{prediction:.2f}**")
