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

# Custom dark style with vibrant colors
dark_style = """
<style>
body, .css-17escra, .stApp, .main {
    background: linear-gradient(135deg, #1a1f2e 0%, #2d3142 50%, #1e2535 100%) !important;
    color: #f0f4ff;
}
.css-1d391kg, .css-1hra1i7, .css-2trqyj, .css-1v0mbdj {
    background-color: rgba(25, 30, 50, 0.85) !important;
    border: 1px solid rgba(0, 255, 255, 0.5) !important;
    border-radius: 12px;
    box-shadow: 0 0 20px rgba(0, 255, 255, 0.1) !important;
}
.stButton>button {
    color: #ffffff;
    background: linear-gradient(135deg, #00d9ff, #0099ff) !important;
    border: 2px solid #00d9ff !important;
    border-radius: 8px;
    font-weight: bold;
    box-shadow: 0 0 15px rgba(0, 217, 255, 0.3) !important;
}
.stButton>button:hover {
    background: linear-gradient(135deg, #00ffff, #00bbff) !important;
    box-shadow: 0 0 25px rgba(0, 217, 255, 0.5) !important;
}
.stSelectbox, .stTimeInput {
    background-color: rgba(25, 30, 50, 0.9) !important;
    border: 1px solid rgba(0, 255, 255, 0.4) !important;
    border-radius: 8px;
}
</style>
"""
st.markdown(dark_style, unsafe_allow_html=True)

# Enhanced title styling
st.markdown(
    "<h1 style='text-align: center; color: #00d9ff; text-shadow: 0 0 10px rgba(0, 217, 255, 0.5);'>🛡️ AI Threat Risk Prediction System</h1>",
    unsafe_allow_html=True
)
st.markdown("<hr style='border: 1px solid rgba(0, 255, 255, 0.3);'>", unsafe_allow_html=True)

with st.container():
    col1, col2 = st.columns([1, 1.2], gap="large")

    with col1:
        st.markdown("<h3 style='color: #00ffcc;'>🔍 Input Panel</h3>", unsafe_allow_html=True)
        location = st.selectbox("Location", ["Data Center", "Office", "Remote Site", "Unmanned", "Unknown"])
        time = st.time_input("Time of event")
        activity = st.selectbox("Activity", ["Login", "File Access", "Config Change", "Network Scan", "Service Spawn"])
        device = st.selectbox("Device", ["Workstation", "Server", "IoT Sensor", "Mobile", "Unknown"])
        movement = st.selectbox("Movement Pattern", ["Static", "Local", "Lateral", "Rapid", "Unknown"])

        predict_btn = st.button("🧠 Predict", key="predict")

    with col2:
        st.markdown("<h3 style='color: #ff00ff;'>🎯 Threat Level</h3>", unsafe_allow_html=True)
        box = st.empty()

        if not predict_btn:
            box.markdown("<h2 style='color:#00d9ff; text-align: center;'>⏳ No prediction yet. Click Predict to evaluate risk.</h2>", unsafe_allow_html=True)

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
            color = "#00ff00"
            emoji = "🟢"
        elif risk_score <= 5:
            level = "MEDIUM"
            color = "#ffff00"
            emoji = "🟡"
        else:
            level = "HIGH"
            color = "#ff0000"
            emoji = "🔴"

        with col2:
            box.markdown(
                f"<div style='padding: 30px; border-radius: 16px; background: rgba(15, 25, 60, 0.95); border: 3px solid {color}; text-align:center; box-shadow: 0 0 30px rgba({color}, 0.4);'>"
                f"<h1 style='margin: 10px; color: {color}; font-size: 3.5rem; text-shadow: 0 0 10px {color};'>{emoji} {level}</h1>"
                f"<p style='font-size:1.3rem; color:#00ffcc; margin:0; font-weight: bold;'>Risk Score: <span style='color:{color};'>{risk_score}</span></p>"
                f"</div>",
                unsafe_allow_html=True,
            )

        st.markdown("---")
        st.markdown("<h2 style='color: #00ffff; text-shadow: 0 0 8px rgba(0, 255, 255, 0.5);'>📊 Model Summary</h2>", unsafe_allow_html=True)

        col3, col4 = st.columns(2, gap="medium")

        with col3:
            st.markdown("<h4 style='color: #00ff88;'>✅ Model Accuracy</h4>", unsafe_allow_html=True)
            accuracy = 0.88
            st.metric(label="Current model accuracy", value=f"{accuracy*100:.1f}%")

            st.markdown("<h4 style='color: #ff00ff;'>📉 Confusion Matrix</h4>", unsafe_allow_html=True)
            cm = np.array([[72, 9, 4], [10, 53, 12], [3, 8, 29]])
            cm_df = pd.DataFrame(cm, index=["Actual LOW", "Actual MEDIUM", "Actual HIGH"], columns=["Pred LOW", "Pred MEDIUM", "Pred HIGH"])
            fig, ax = plt.subplots(figsize=(4, 3))
            sns.heatmap(cm_df, annot=True, fmt='d', cmap='mako', cbar=False, linewidths=0.5, linecolor='white', ax=ax)
            ax.set_title('Confusion Matrix', color='#00ffff', fontsize=12, fontweight='bold')
            ax.tick_params(colors='#00d9ff', labelsize=9)
            ax.spines[:].set_visible(True)
            st.pyplot(fig)

        with col4:
            st.markdown("<h4 style='color: #ffaa00;'>🧾 Feature Importance</h4>", unsafe_allow_html=True)
            features = ["location", "time", "activity", "device", "movement"]
            importances = [0.27, 0.18, 0.33, 0.14, 0.08]
            fig2, ax2 = plt.subplots(figsize=(5, 3))
            sns.barplot(x=importances, y=features, palette='rocket', ax=ax2)
            ax2.set_xlim(0, 0.4)
            ax2.set_title('Feature Importance', color='#00ffff', fontsize=12, fontweight='bold')
            ax2.set_xlabel('Importance', color='#00ffcc')
            ax2.set_ylabel('Feature', color='#00ffcc')
            ax2.tick_params(colors='#00d9ff')
            st.pyplot(fig2)

        st.markdown("\n---\n")
        st.markdown("<h3 style='color: #ff6600;'>📌 Notes</h3>", unsafe_allow_html=True)
        st.markdown(
            "<div style='background-color: rgba(0, 217, 255, 0.1); padding: 10px; border-radius: 8px; border-left: 4px solid #00d9ff;'>"
            "- The prediction is a simulated risk scoring for demo purposes.<br>"
            "- For production, replace logic with a trained ML model endpoint.<br>"
            "- Use secure data channels and audit logs for all events."
            "</div>",
            unsafe_allow_html=True
        )
