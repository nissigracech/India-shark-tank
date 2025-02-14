import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly
from PIL import Image
import streamlit.components.v1 as components  

 
# Set page config
st.set_page_config(page_title="Shark Tank India EDA Dashboard", layout="wide")

# Initialize session state for button selection
if "selected_button" not in st.session_state:
    st.session_state.selected_button = None

# Function to handle button clicks
def set_active_button(button_key):
    st.session_state.selected_button = button_key

# Apply styles dynamically based on active button
selected_s1 = "#1e6899" if st.session_state.selected_button == "s1" else "#FFD700"
selected_s2 = "#1e6899" if st.session_state.selected_button == "s2" else "transparent"
selected_s3 = "#1e6899" if st.session_state.selected_button == "s3" else "transparent"

selected_text_s1 = "white" if st.session_state.selected_button == "s1" else "black"
selected_text_s2 = "white" if st.session_state.selected_button == "s2" else "#00A8E8"
selected_text_s3 = "white" if st.session_state.selected_button == "s3" else "white"

st.markdown(f"""
    <style>
        /* Set full-page background */
        body {{
            background: linear-gradient(135deg, #002147, #0096FF) !important;
            color: white !important;
        }}

        /* Button styling */
        .stButton>button {{
            width: 150px;
            font-weight: bold;
            font-size: 16px;
            padding: 10px;
            border-radius: 8px;
            border: 2px solid transparent;
            cursor: pointer;
            text-align: center;
            transition: all 0.3s ease-in-out;
        }}

        /* Season 1 Button - Active & Hover */
        .season1 {{
            background-color: {selected_s1} !important;
            color: {selected_text_s1} !important;
            border-color: {selected_s1} !important;
        }}
        .season1:hover {{
            background-color: #1e6899 !important;
            color: white !important;
            border-color: #1e6899 !important;
        }}

        /* Season 2 Button - Active & Hover */
        .season2 {{
            background-color: {selected_s2} !important;
            color: {selected_text_s2} !important;
            border-color: #00A8E8 !important;
        }}
        .season2:hover {{
            background-color: #1e6899 !important;
            color: white !important;
            border-color: #1e6899 !important;
        }}

        /* Season 3 Button - Active & Hover */
        .season3 {{
            background-color: {selected_s3} !important;
            color: {selected_text_s3} !important;
            border-color: white !important;
        }}
        .season3:hover {{
            background-color: #1e6899 !important;
            color: white !important;
            border-color: #1e6899 !important;
        }}
    </style>
""", unsafe_allow_html=True)

# Create 3 main columns (Left empty, Center with buttons, Right empty)
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Create another row of columns inside col2 for buttons
    sub_col1, sub_col2, sub_col3 = st.columns(3)

    with sub_col1:
        if st.button("Season 1", key="s1", on_click=set_active_button, args=("s1",)):
            pass

    with sub_col2:
        if st.button("Season 2", key="s2", on_click=set_active_button, args=("s2",)):
            pass

    with sub_col3:
        if st.button("Season 3", key="s3", on_click=set_active_button, args=("s3",)):
            pass

# Handling button clicks
if st.session_state.selected_button == "s1":
    st.write("### 📊 Season 1 Analysis!")
elif st.session_state.selected_button == "s2":
    st.write("### 📊 Season 2 Analysis!")
elif st.session_state.selected_button == "s3":
    st.write("### 📊 Season 3 Analysis!")
