import streamlit as st
import numpy as np
import pickle
from db import save_prediction

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(page_title="Heart Disease Prediction", layout="wide")

# -------------------------
# CUSTOM CSS
# -------------------------
st.markdown("""
<style>
.stApp {
    background-color: #000000;
    color: #ffffff;
}

h1, h2, h3, p, label {
    color: #ffffff !important;
}

.stButton>button {
    background-color: #00ff88 !important;
    color: black !important;
    border-radius: 8px;
    font-weight: bold;
}

input, div[data-baseweb="select"] > div {
    background-color: #111111 !important;
    color: white !important;
}
</style>
""", unsafe_allow_html=True)

# -------------------------


# -------------------------
# LOAD MODEL
# -------------------------
model = pickle.load(open('model.pkl', 'rb'))

# -------------------------
# TITLE
# -------------------------
st.markdown("<h1>❤️ Heart Disease Prediction</h1>", unsafe_allow_html=True)
st.markdown("<h3>Enter patient details</h3>", unsafe_allow_html=True)

# -------------------------
# INPUT SECTION
# -------------------------
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", 1, 120, 50)
    sex = st.selectbox("Sex", [0, 1])
    cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
    trestbps = st.number_input("Resting BP", value=120)
    chol = st.number_input("Cholesterol", value=200)
    fbs = st.selectbox("Fasting Sugar > 120", [0, 1])

with col2:
    restecg = st.selectbox("Rest ECG", [0, 1, 2])
    thalach = st.number_input("Max Heart Rate", value=150)
    exang = st.selectbox("Exercise Angina", [0, 1])
    oldpeak = st.number_input("ST Depression", value=1.0)
    slope = st.selectbox("Slope", [0, 1, 2])
    ca = st.selectbox("Vessels (0-3)", [0, 1, 2, 3])
    thal = st.selectbox("Thal", [1, 2, 3])

# -------------------------
# PREDICTION
# -------------------------
if st.button("🚀 Predict"):

    input_data = np.array([[age, sex, cp, trestbps, chol, fbs,
                            restecg, thalach, exang, oldpeak,
                            slope, ca, thal]])

    prediction = model.predict(input_data)

    # -------------------------
    # RESULT
    # -------------------------
    if prediction[0] == 1:
        st.error("⚠️ High Risk of Heart Disease")
    else:
        st.success("✅ Low Risk of Heart Disease")

    # -------------------------
    # SAVE TO MYSQL
    # -------------------------
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO heart_predictions 
        (age, sex, cp, trestbps, chol, prediction)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (age, sex, cp, trestbps, chol, int(prediction[0])))

    conn.commit()
