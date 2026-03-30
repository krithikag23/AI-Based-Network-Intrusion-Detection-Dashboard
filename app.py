import streamlit as st
import pandas as pd
from model import train_model
from log_analyzer import detect_suspicious_logs


st.title("🔐 AI Intrusion Detection System")

model = train_model()


st.subheader("Enter Network Traffic Data")

duration = st.number_input("Duration", value=1)
src_bytes = st.number_input("Source Bytes", value=100)
dst_bytes = st.number_input("Destination Bytes", value=200)

if st.button("Predict"):
    input_data = pd.DataFrame([[duration, src_bytes, dst_bytes]],
                              columns=["duration", "src_bytes", "dst_bytes"])
    
    prediction = model.predict(input_data)[0]
    
    if prediction == "attack":
        st.error("⚠️ Intrusion Detected!")
    else:
        st.success("✅ Normal Traffic")


st.subheader("📄 Log Analyzer")

log_input = st.text_area("Paste system/network logs here")

if st.button("Analyze Logs"):
    alerts = detect_suspicious_logs(log_input)

    if alerts:
        st.error("⚠️ Suspicious Activity Detected!")
        for alert in alerts:
            st.write("🚨 " + alert)
    else:
        st.success("✅ No suspicious activity found")


import time
from simulator import generate_traffic

st.subheader("📡 Real-Time Traffic Monitor")

run_simulation = st.checkbox("Start Live Monitoring")

if run_simulation:
    st.info("Monitoring live traffic...")

    for i in range(10):  # simulate 10 packets
        sample = generate_traffic()
        prediction = model.predict(sample)[0]

        st.write(f"Packet {i+1}: {sample.to_dict(orient='records')[0]}")

        if prediction == "attack":
            st.error("🚨 ALERT: Intrusion Detected!")
        else:
            st.success("✅ Normal Traffic")

        time.sleep(1)

from deep_model import train_autoencoder, detect_anomaly
import numpy as np

st.subheader("🧠 Deep Learning Anomaly Detection")

# Train on normal data only
normal_data = np.array([
    [10, 100, 200],
    [5, 300, 400],
])

autoencoder = train_autoencoder(normal_data)

if st.button("Run Deep Detection"):
    sample = generate_traffic().values
    is_anomaly, error = detect_anomaly(autoencoder, sample)

    st.write(f"Reconstruction Error: {error:.5f}")

    if is_anomaly:
        st.error("🚨 Anomaly Detected (Possible Unknown Attack)")
    else:
        st.success("✅ Normal Behavior")

import matplotlib.pyplot as plt

st.subheader("📊 Traffic Analytics")

if st.button("Generate Analytics"):
    labels = ["Normal", "Attack"]
    values = [7, 3]  # simulated counts

    fig, ax = plt.subplots()
    ax.pie(values, labels=labels, autopct='%1.1f%%')
    st.pyplot(fig)
