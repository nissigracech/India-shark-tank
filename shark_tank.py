import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly


# Set page config
st.set_page_config(page_title="Shark Tank India EDA Dashboard", layout="wide")

# Custom CSS for styling (Sidebar styles removed)
st.markdown("""
    <style>
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
        }

        /* Season 1 Button - Filled Yellow */
        .season1 {
            background-color: #FFD700 !important;
            color: black !important;
            border-color: #FFD700 !important;
        }

        /* Season 2 Button - Blue Outline */
        .season2 {
            background-color: transparent !important;
            color: #00A8E8 !important;
            border: 2px solid #00A8E8 !important;
        }

        /* Season 3 Button - White Outline */
        .season3 {
            background-color: transparent !important;
            color: white !important;
            border: 2px solid white !important;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="title">SHARK TANK INDIA</h1>', unsafe_allow_html=True)

# Create 3 main columns (Left empty, Center with buttons, Right empty)
col1, col2, col3 = st.columns([1, 2, 1])  # Adjust width to center buttons

with col2:
    # Create another row of columns inside col2 for buttons
    sub_col1, sub_col2, sub_col3 = st.columns(3)

    with sub_col1:
        season1 = st.button("Season 1", key="s1")

    with sub_col2:
        season2 = st.button("Season 2", key="s2")

    with sub_col3:
        season3 = st.button("Season 3", key="s3")

# Handling button clicks
if season1:
    st.write("### 📊 Season 1 Analysis!")

if season2:
    st.write("### 📊 Season 2 Analysis!")

if season3:
    st.write("### 📊 Season 3 Analysis!")
