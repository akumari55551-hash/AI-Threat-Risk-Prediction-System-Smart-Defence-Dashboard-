import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="AI Threat Risk Prediction System",
    page_icon="🛡️",
    layout="wide",
)

# Custom dark style
dark_style = """
<style>
body, .css-17escra, .stApp, .main {
    background: linear-gradient(135deg, #020512 0%, #111d42 40%, #1e237a 100%) !important;
    color: #e6e6ff;
}
.css-1d391kg, .css-1hra1i7, .css-2trqyj, .css-1v0mbdj {
    background-color: rgba(7, 13, 47, 0.90) !important;
    border: 1px solid rgba(120, 160, 255, 0.35);
    border-radius: 12px;
}
.stButton>button {
    color: #edf2ff;
    background: linear-gradient(135deg, #0b3d91, #261f6f);
    border: 1px solid #5172c6;
}
</style>
"""
st.markdown(dark_style, unsafe_allow_html=True)

st.markdown("# 🛡️ AI Threat Risk Prediction System")
st.markdown("---")

with st.container():
    col1, col2 = st.columns([1, 1.2], gap="large")

    with col1:
        st.markdown("### 🔍 Input Panel")
        location = st.selectbox("Location", ["Data Center", "Office", "Remote Site", "Unmanned", "Unknown"])
        time = st.time_input("Time of event")
        activity = st.selectbox("Activity", ["Login", "File Access", "Config Change", "Network Scan", "Service Spawn"])
        device = st.selectbox("Device", ["Workstation", "Server", "IoT Sensor", "Mobile", "Unknown"])
        movement = st.selectbox("Movement Pattern", ["Static", "Local", "Lateral", "Rapid", "Unknown"])

        predict_btn = st.button("🧠 Predict", key="predict")

    with col2:
        st.markdown("### 🎯 Threat Level")
        box = st.empty()

        if not predict_btn:
            box.markdown("<h2 style='color:#9da7ff'>No prediction yet. Click Predict to evaluate risk.</h2>", unsafe_allow_html=True)

    if predict_btn:
        risk_score = 0
        if location in ["Unmanned", "Unknown"]:
            risk_score += 1
        if activity in ["Network Scan", "Service Spawn"]:
            risk_score += 2
        if device in ["IoT Sensor", "Mobile", "Unknown"]:
            risk_score += 1
        if movement in ["Lateral", "Rapid"]:
            risk_score += 2
        hour = time.hour
        if 0 <= hour < 6 or 22 <= hour <= 23:
            risk_score += 1

        if risk_score <= 2:
            level = "LOW"
            color = "#2ecc71"
            emoji = "🟢"
        elif risk_score <= 5:
            level = "MEDIUM"
            color = "#f1c40f"
            emoji = "🟡"
        else:
            level = "HIGH"
            color = "#e74c3c"
            emoji = "🔴"

        with col2:
            box.markdown(
                f"<div style='padding: 24px; border-radius: 16px; background: rgba(20, 26, 65, 0.82); border: 2px solid {color}; text-align:center;'>"
                f"<h1 style='margin: 10px; color: {color}; font-size: 3.4rem;'>{emoji} {level}</h1>"
                f"<p style='font-size:1.2rem; color:#dde6ff; margin:0;'>Threat risk score: <strong>{risk_score}</strong></p>"
                f"</div>",
                unsafe_allow_html=True,
            )

        st.markdown("---")
        st.markdown("### 📊 Model Summary")

        col3, col4 = st.columns(2, gap="medium")

        with col3:
            st.markdown("#### ✅ Model Accuracy")
            accuracy = 0.88
            st.metric(label="Current model accuracy", value=f"{accuracy*100:.1f}%")

            st.markdown("#### 📉 Confusion Matrix")
            cm = np.array([[72, 9, 4], [10, 53, 12], [3, 8, 29]])
            cm_df = pd.DataFrame(cm, index=["Actual LOW", "Actual MEDIUM", "Actual HIGH"], columns=["Pred LOW", "Pred MEDIUM", "Pred HIGH"])
            fig, ax = plt.subplots(figsize=(4, 3))
            sns.heatmap(cm_df, annot=True, fmt='d', cmap='mako', cbar=False, linewidths=0.5, linecolor='white', ax=ax)
            ax.set_title('Confusion Matrix', color='#edf2ff')
            ax.tick_params(colors='#edf2ff', labelsize=9)
            ax.spines[:].set_visible(True)
            st.pyplot(fig)

        with col4:
            st.markdown("#### 🧾 Feature Importance")
            features = ["location", "time", "activity", "device", "movement"]
            importances = [0.27, 0.18, 0.33, 0.14, 0.08]
            fig2, ax2 = plt.subplots(figsize=(5, 3))
            sns.barplot(x=importances, y=features, palette='viridis', ax=ax2)
            ax2.set_xlim(0, 0.4)
            ax2.set_title('Feature Importance', color='#edf2ff')
            ax2.set_xlabel('Importance', color='#c8d3f9')
            ax2.set_ylabel('Feature', color='#c8d3f9')
            ax2.tick_params(colors='#edf2ff')
            st.pyplot(fig2)

        st.markdown("\n---\n")
        st.markdown("### 📌 Notes")
        st.markdown(
            "- The prediction is a simulated risk scoring for demo purposes.\n"
            "- For production, replace logic with a trained ML model endpoint.\n"
            "- Use secure data channels and audit logs for all events."
        )
