import streamlit as st

# Set page config
st.set_page_config(page_title="Shark Tank India EDA Dashboard", layout="wide")

# Centered bold title
st.markdown("""
    <style>
        .title {
            text-align: center;
            font-weight: bold;
            font-size: 2em;
        }
    </style>
    <h1 class="title">Shark Tank India EDA Dashboard</h1>
""", unsafe_allow_html=True)