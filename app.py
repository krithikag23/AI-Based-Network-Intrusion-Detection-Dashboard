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
