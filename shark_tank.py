import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly
from PIL import Image
import streamlit.components.v1 as components  


# Set page config
st.set_page_config(page_title="Shark Tank India EDA Dashboard", layout="wide")

# Custom CSS for background, title, and buttons
st.markdown("""
    <style>
        /* Set full-page background */
        body {
            background: linear-gradient(135deg, #002147, #0096FF) !important;
            color: white !important;
        }

        /* Centered bold uppercase yellow title */
        .title {
            text-align: center;
            font-weight: 900;
            font-size: 5em;
            color: #FFD700; /* Gold Yellow */
            text-transform: uppercase;
        }

        /* Button styling */
        .stButton>button {
            width: 150px;
            font-weight: bold;
            font-size: 16px;
            padding: 10px;
            border-radius: 8px;
            border: 2px solid transparent;
            cursor: pointer;
            text-align: center;
            transition: all 0.3s ease-in-out;
        }

        /* Season 1 Button - Filled Yellow */
        .stButton>button:first-of-type {
            background-color: #FFD700 !important;
            color: black !important;
            border-color: #FFD700 !important;
        }

        /* Season 2 Button - Blue Outline */
        .stButton>button:nth-of-type(2) {
            background-color: transparent !important;
            color: #00A8E8 !important;
            border: 2px solid #00A8E8 !important;
        }

        /* Season 3 Button - White Outline */
        .stButton>button:nth-of-type(3) {
            background-color: transparent !important;
            color: white !important;
            border: 2px solid white !important;
        }

        /* Hover effect for ALL buttons */
        .stButton>button:hover {
            background-color: #1e6899 !important;
            color: white !important;
            border-color: #1e6899 !important;
        }

        /* Clicked (active) effect */
        .stButton>button:active, 
        .stButton>button.selected {
            background-color: #1e6899 !important;
            color: white !important;
            border-color: #1e6899 !important;
        }
    </style>
""", unsafe_allow_html=True)

# Display Images in two columns (1:4 ratio)
col1, col2 = st.columns([1, 4])

with col1:
    st.image("stilogo.png", caption=" ", width=150)  # Smaller Image

with col2:
    st.image("st.png", caption=" ", width=600)  # Larger Image

# Create 3 main columns for button alignment
col1, col2, col3 = st.columns([1, 2, 1])  

with col2:
    # Create sub-columns for buttons
    sub_col1, sub_col2, sub_col3 = st.columns(3)

    # Initialize session state for button selection
    if 'selected_button' not in st.session_state:
        st.session_state.selected_button = None

    # Define button actions
    with sub_col1:
        if st.button("Season 1", key="s1"):
            st.session_state.selected_button = "s1"

    with sub_col2:
        if st.button("Season 2", key="s2"):
            st.session_state.selected_button = "s2"

    with sub_col3:
        if st.button("Season 3", key="s3"):
            st.session_state.selected_button = "s3"

# Handling button clicks
if st.session_state.selected_button == "s1":
    st.write("### 📊 Season 1 Analysis!")
elif st.session_state.selected_button == "s2":
    st.write("### 📊 Season 2 Analysis!")
elif st.session_state.selected_button == "s3":
    st.write("### 📊 Season 3 Analysis!")
