import streamlit as st
from PyPDF2 import PdfReader
from transformers import pipeline

# Load summarizer model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

st.title("📄 Smart Research Paper Summarizer")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")
