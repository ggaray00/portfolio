import streamlit as st
import pandas as pd

if "authenticated" not in st.session_state or not st.session_state.authenticated:
    st.warning("🔒 Please login from the main page to access this page.")
    st.stop()


st.title("📊 Data Analysis")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())

    st.write("### Basic Statistics")
    st.write(df.describe())

    st.write("### Data Visualization")
    st.bar_chart(df.select_dtypes(include='number'))
