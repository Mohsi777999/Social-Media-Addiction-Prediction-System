import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open("model/addiction_model.pkl", "rb"))
st.title("Social Media Addiction Prediction")
st.write("Enter user details to predict addiction level.")
# User inputs
age = st.slider("Age", 15, 40, 20)
screen_time = st.slider("Daily Screen Time (Hours)", 1, 15, 5)
sleep_hours = st.slider("Sleep Hours", 1, 12, 7)
study_hours = st.slider("Study Hours", 0, 12, 4)
productivity = st.selectbox(
    "Productivity Level",
    ["Low", "Medium", "High"]
)
# Convert productivity into numbers
productivity_map = {
    "Low": 0,
    "Medium": 1,
    "High": 2
}
productivity_value = productivity_map[productivity]
if st.button("Predict Addiction"):
    sample = pd.DataFrame(
        [[age, screen_time, sleep_hours, study_hours, productivity_value]],
        columns=[
            "Age",
            "Daily_Screen_Time",
            "Sleep_Hours",
            "Study_Hours",
            "Productivity_Level"
        ]
    )
    prediction = model.predict(sample)
    # Convert prediction to label
    result_map = {
        0: "High Addiction",
        1: "Low Addiction",
        2: "Medium Addiction"
    }
    result = result_map[prediction[0]]
    st.subheader("Prediction Result")
    st.success(result)