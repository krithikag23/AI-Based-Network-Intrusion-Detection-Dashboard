import streamlit as st
import pandas as pd
from model import train_model

st.title("🔐 AI Intrusion Detection System")

model = train_model()
