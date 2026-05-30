import os
import pickle
import streamlit as st
import pandas as pd

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Smart Crop Recommendation System",
    page_icon="🌾",
    layout="wide"
)

# -----------------------------
# Load Model
# -----------------------------
BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "models",
    "crop_model.pkl"
)

with open(MODEL_PATH, "rb") as file:
    model = pickle.load(file)

# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:
    st.title("🌾 Project Information")

    st.markdown("""
    ### Smart Crop Recommendation

    This system predicts the most suitable crop based on:

    - Nitrogen (N)
    - Phosphorus (P)
    - Potassium (K)
    - Temperature
    - Humidity
    - pH Value
    - Rainfall

    ### Machine Learning Model
    - Random Forest Classifier

    ### Accuracy
    - 99.55%
    """)

# -----------------------------
# Header
# -----------------------------
st.title("🌾 Smart Crop Recommendation System")

st.markdown(
    "Predict the most suitable crop based on soil nutrients and climatic conditions."
)

# -----------------------------
# Dashboard Metrics
# -----------------------------
metric1, metric2, metric3 = st.columns(3)

metric1.metric(
    label="Model Accuracy",
    value="99.55%"
)

metric2.metric(
    label="Supported Crops",
    value="22"
)

metric3.metric(
    label="Algorithm",
    value="Random Forest"
)

st.markdown("---")

# -----------------------------
# Input Section
# -----------------------------
st.subheader("📥 Enter Soil & Weather Parameters")

col1, col2 = st.columns(2)

with col1:
    nitrogen = st.number_input(
        "Nitrogen (N)",
        min_value=0.0,
        value=90.0
    )

    phosphorus = st.number_input(
        "Phosphorus (P)",
        min_value=0.0,
        value=42.0
    )

    potassium = st.number_input(
        "Potassium (K)",
        min_value=0.0,
        value=43.0
    )

    temperature = st.number_input(
        "Temperature (°C)",
        value=20.8
    )

with col2:
    humidity = st.number_input(
        "Humidity (%)",
        value=82.0
    )

    ph = st.number_input(
        "pH Value",
        value=6.5
    )

    rainfall = st.number_input(
        "Rainfall (mm)",
        value=202.0
    )

st.markdown("")

predict_btn = st.button(
    "🌱 Recommend Crop",
    use_container_width=True
)

# -----------------------------
# Prediction
# -----------------------------
if predict_btn:

    sample = pd.DataFrame(
        [[
            nitrogen,
            phosphorus,
            potassium,
            temperature,
            humidity,
            ph,
            rainfall
        ]],
        columns=[
            "N",
            "P",
            "K",
            "temperature",
            "humidity",
            "ph",
            "rainfall"
        ]
    )

    prediction = model.predict(sample)[0]

    probabilities = model.predict_proba(sample)[0]

    classes = model.classes_

    top_3 = sorted(
        zip(classes, probabilities),
        key=lambda x: x[1],
        reverse=True
    )[:3]

    best_crop = top_3[0][0]
    best_confidence = top_3[0][1]

    st.markdown("---")

    st.subheader("🌾 Recommended Crop")

    st.markdown(
        f"""
        <div style="
            background-color:#1e5631;
            padding:25px;
            border-radius:12px;
            text-align:center;
            color:white;
            font-size:32px;
            font-weight:bold;
        ">
            {prediction.upper()}
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("")

    st.metric(
        "Prediction Confidence",
        f"{best_confidence:.2%}"
    )

    st.markdown("---")

    st.subheader("🏆 Top 3 Crop Recommendations")

    medals = ["🥇", "🥈", "🥉"]

    for i, (crop, prob) in enumerate(top_3):

        st.write(
            f"{medals[i]} {crop.title()} ({prob:.2%})"
        )

        st.progress(float(prob))

# -----------------------------
# Feature Importance
# -----------------------------
feature_path = os.path.join(
    BASE_DIR,
    "reports",
    "feature_importance.png"
)

if os.path.exists(feature_path):

    st.markdown("---")

    st.subheader("📊 Feature Importance")

    st.image(
        feature_path,
        use_container_width=True
    )

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")

st.info(
    "Machine Learning Mini Project | Random Forest Classifier | Accuracy: 99.55%"
)
