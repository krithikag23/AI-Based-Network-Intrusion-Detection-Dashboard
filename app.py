import streamlit as st
import pandas as pd
from model import train_model

st.title("🔐 AI Intrusion Detection System")

model = train_model()


st.subheader("Enter Network Traffic Data")

duration = st.number_input("Duration", value=1)
src_bytes = st.number_input("Source Bytes", value=100)
dst_bytes = st.number_input("Destination Bytes", value=200)
