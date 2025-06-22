# app.py
import streamlit as st
import pandas as pd
from model import train_isolation_forest, predict_anomalies

st.set_page_config(page_title="Anomaly Detection", layout="wide")

st.title("🔍 Anomaly Detection with Isolation Forest")

uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file:
    data = pd.read_csv(uploaded_file)
    st.write("📊 Uploaded Data", data.head())

    contamination = st.slider("Select Contamination Rate", 0.01, 0.3, 0.05, step=0.01)

    if st.button("Run Anomaly Detection"):
        model = train_isolation_forest(data, contamination)
        result = predict_anomalies(model, data)
        st.success("✅ Detection complete.")
        st.write("🚨 Anomaly Results", result)
        st.download_button("📥 Download Result", result.to_csv(index=False), "anomaly_result.csv", "text/csv")
else:
    st.info("👆 Upload a CSV file to get started.")
