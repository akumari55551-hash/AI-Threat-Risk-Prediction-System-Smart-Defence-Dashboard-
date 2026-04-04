import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(
    page_title="AI Threat Risk Prediction System",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom dark theme CSS
dark_theme_css = """
<style>
body, .stApp, .main {
    background-color: #0e1117 !important;
    color: #ffffff;
}
.css-1d391kg, .css-1hra1i7, .css-2trqyj, .css-1v0mbdj {
    background-color: rgba(13, 17, 23, 0.95) !important;
    border: 1px solid rgba(0, 123, 255, 0.3);
    border-radius: 12px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.3);
}
.stButton>button {
    background: linear-gradient(135deg, #00d4ff, #0099cc);
    color: #ffffff;
    border: none;
    border-radius: 8px;
    padding: 12px 24px;
    font-weight: bold;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}
.stButton>button:hover {
    background: linear-gradient(135deg, #0099cc, #0077aa);
}
.stSelectbox, .stTimeInput {
    background-color: rgba(13, 17, 23, 0.9) !important;
    border: 1px solid rgba(0, 123, 255, 0.3);
    border-radius: 8px;
}
.stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
    color: #00d4ff;
}
.stMetric {
    background-color: rgba(13, 17, 23, 0.8);
    border-radius: 8px;
    padding: 10px;
}
</style>
"""
st.markdown(dark_theme_css, unsafe_allow_html=True)

# Header Section
st.markdown("# 🛡️ AI Threat Risk Prediction System")
st.markdown("### Real-time threat analysis and risk classification")
st.markdown("---")

# Main Section - Two Columns
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("### 📥 Input Parameters")
    with st.container():
        st.markdown("**🏢 Location**")
        location = st.selectbox("", ["Data Center", "Office", "Remote Site", "Unmanned", "Unknown"], key="location")
        
        st.markdown("**⏰ Time**")
        time_options = [f"{h:02d}:00" for h in range(24)]
        time = st.selectbox("", time_options, key="time")
        
        st.markdown("**🔧 Activity Type**")
        activity = st.selectbox("", ["Login", "File Access", "Config Change", "Network Scan", "Service Spawn"], key="activity")
        
        st.markdown("**💻 Device Type**")
        device = st.selectbox("", ["Workstation", "Server", "IoT Sensor", "Mobile", "Unknown"], key="device")
        
        st.markdown("**🚶 Movement Pattern**")
        movement = st.selectbox("", ["Static", "Local", "Lateral", "Rapid", "Unknown"], key="movement")
        
        st.markdown("")
        predict_btn = st.button("🔍 Predict Threat", key="predict")

with col2:
    st.markdown("### 🎯 Threat Assessment")
    with st.container():
        if not predict_btn:
            st.markdown(
                "<div style='text-align: center; padding: 40px; background-color: rgba(13, 17, 23, 0.8); border-radius: 12px; border: 2px solid #00d4ff;'>"
                "<h2 style='color: #00d4ff; margin: 0;'>Awaiting Analysis</h2>"
                "<p style='color: #cccccc; margin: 10px 0 0 0;'>Click 'Predict Threat' to evaluate risk level</p>"
                "</div>",
                unsafe_allow_html=True
            )
        else:
            # Simulated result - in real app, this would come from model
            threat_level = "HIGH"  # Placeholder
            color = "#e74c3c" if threat_level == "HIGH" else "#f1c40f" if threat_level == "MEDIUM" else "#2ecc71"
            emoji = "🔴" if threat_level == "HIGH" else "🟡" if threat_level == "MEDIUM" else "🟢"
            description = "Unusual activity detected" if threat_level == "HIGH" else "Moderate risk observed" if threat_level == "MEDIUM" else "Normal activity"
            
            st.markdown(
                f"<div style='text-align: center; padding: 40px; background-color: rgba(13, 17, 23, 0.8); border-radius: 12px; border: 2px solid {color};'>"
                f"<h1 style='color: {color}; margin: 0; font-size: 3rem;'>{emoji} {threat_level}</h1>"
                f"<p style='color: #cccccc; margin: 10px 0 0 0; font-size: 1.1rem;'>{description}</p>"
                "</div>",
                unsafe_allow_html=True
            )

# Insights Section
st.markdown("---")
st.markdown("### 📊 System Insights")

col3, col4 = st.columns(2, gap="medium")

with col3:
    st.markdown("#### ✅ Model Accuracy")
    accuracy = 0.92  # Placeholder
    st.metric(label="Overall Accuracy", value=f"{accuracy*100:.1f}%")
    
    st.markdown("#### 📈 Feature Importance")
    # Placeholder bar chart
    features = ["Location", "Time", "Activity", "Device", "Movement"]
    importances = [0.25, 0.20, 0.30, 0.15, 0.10]
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.barh(features, importances, color='#00d4ff')
    ax.set_xlim(0, 0.35)
    ax.set_title('Feature Importance', color='#ffffff')
    ax.set_xlabel('Importance', color='#cccccc')
    ax.set_ylabel('Feature', color='#cccccc')
    ax.tick_params(colors='#cccccc')
    ax.spines[:].set_visible(False)
    fig.patch.set_facecolor('#0e1117')
    ax.set_facecolor('#0e1117')
    st.pyplot(fig)

with col4:
    st.markdown("#### 📋 Confusion Matrix")
    # Placeholder confusion matrix
    cm = np.array([[85, 8, 2], [12, 68, 5], [1, 4, 35]])
    cm_df = pd.DataFrame(cm, index=["Actual LOW", "Actual MEDIUM", "Actual HIGH"], columns=["Pred LOW", "Pred MEDIUM", "Pred HIGH"])
    fig2, ax2 = plt.subplots(figsize=(4, 3))
    sns.heatmap(cm_df, annot=True, fmt='d', cmap='coolwarm', cbar=False, linewidths=0.5, linecolor='#ffffff', ax=ax2)
    ax2.set_title('Confusion Matrix', color='#ffffff')
    ax2.tick_params(colors='#cccccc', labelsize=8)
    ax2.spines[:].set_visible(False)
    fig2.patch.set_facecolor('#0e1117')
    ax2.set_facecolor('#0e1117')
    st.pyplot(fig2)

# Footer
st.markdown("---")
st.markdown("*Dashboard designed for cybersecurity monitoring and threat assessment.*")
