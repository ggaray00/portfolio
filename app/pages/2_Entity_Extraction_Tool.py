import streamlit as st
import pandas as pd
import pdfplumber
from annotated_text import annotated_text
from huggingface_hub import InferenceClient



if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("🔒 Please login from the main page to access this page.")
    st.stop()

client = InferenceClient("dslim/distilbert-NER", token=st.secrets["all_token"])

def viz_entities(text):
    entities = client.token_classification(text)
    for entity in entities:
        annotated_text(
            text[:entity["start"]],
            (text[entity["start"]:entity["end"]], entity["entity"]),
            text[entity["end"]:]
        )


st.title("🔎 Entity Extraction Tool")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
if uploaded_file:
    with pdfplumber.open(uploaded_file) as pdf:
        text = ''
        for page in pdf.pages:
            text += page.extract_text()

    st.write(text)
    viz_entities(text)

