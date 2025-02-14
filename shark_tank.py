import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly
from PIL import Image
import streamlit.components.v1 as components  

def classes(argument):
        st.markdown(f"<h1 style='text-align: center;'>{argument}</h1>", unsafe_allow_html=True)
        #st.write(argument)
        st.subheader("hello the function is working")

# Set page config
st.set_page_config(page_title="Shark Tank India EDA Dashboard", layout="wide")

# Custom CSS for styling (Sidebar styles removed)
st.markdown("""
    <style>
    /* Full page background color */
        body, .stApp {
            background-color: #292b32 !important;
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
            border: 2px solid #0a91bd !important; /* Blue Border */
            cursor: pointer;
            text-align: center;
            background-color: transparent !important;
            color: white !important;
        }

        /* Hover effect */
        .stButton>button:hover {
            background-color: rgba(10, 145, 189, 0.2) !important; /* Light Blue on Hover */
        }

        /* Active effect (Clicked button remains yellow) */
        .stButton>button:active {
            background-color: #FFD700 !important; /* Yellow */
            color: black !important;
            border-color: #FFD700 !important;
        }
    </style>
""", unsafe_allow_html=True)


col1, col2, col3 = st.columns([4,1, 15])  

with col1:
    st.image("stilogo.png", caption=" " , width=400)  # Smaller Image

with col3:
    st.image("st.png", caption=" ", width=1000)  # Larger Image

'''
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
    argument="### 📊 Season 1 Analysis!"
    classes(argument)
    #st.write("### 📊 Season 1 Analysis!")

if season2:
    argument="### 📊 Season 2 Analysis!"
    classes(argument)
    #st.write("### 📊 Season 2 Analysis!")

if season3:
    argument="### 📊 Season 3 Analysis!"
    classes(argument)
    #st.write("### 📊 Season 3 Analysis!")

'''
 

# Create three columns with different widths
col1, col2, col3 = st.columns([1, 2, 1])  

# Add a full-width box in each column
with col1:
    st.markdown("<div style='background-color: red; padding: 20px; text-align: center;'>Column 1</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div style='background-color: blue; padding: 20px; text-align: center;'>Column 2</div>", unsafe_allow_html=True)

with col3:
    st.markdown("<div style='background-color: green; padding: 20px; text-align: center;'>Column 3</div>", unsafe_allow_html=True)

 

# Create three main columns (col2 is wider)
col1, col2, col3 = st.columns([1, 2, 1])  

with col2:
    # Create three equal sub-columns inside col2
    sub_col1, sub_col2, sub_col3 = st.columns(3)

    # Centering buttons using Markdown & CSS
    with sub_col1:
        st.markdown("<div style='text-align: center;'><button class='stButton'>Button 1</button></div>", unsafe_allow_html=True)

    with sub_col2:
        st.markdown("<div style='text-align: center;'><button class='stButton'>Button 2</button></div>", unsafe_allow_html=True)

    with sub_col3:
        st.markdown("<div style='text-align: center;'><button class='stButton'>Button 3</button></div>", unsafe_allow_html=True)

# Create 3 main columns (Left empty, Center with buttons, Right empty)
col1, col2, col3 = st.columns([1, 2, 1])  # Adjust width to center buttons

with col2:
    # Create another row of columns inside col2 for buttons
    sub_col1, sub_col2, sub_col3,sub_col4,sub_col5,sub_col6,sub_col7 = st.columns([1, 1,1,1,1,1,1])  # Equal width columns

    with sub_col1:
        st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
        season1 = st.button("Season 1", key="s1")
        st.markdown("</div>", unsafe_allow_html=True)

    with sub_col2:
        st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
        season2 = st.button("Season 2", key="s2")
        st.markdown("</div>", unsafe_allow_html=True)

    with sub_col3:
        st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
        season3 = st.button("Season 3", key="s3")
        st.markdown("</div>", unsafe_allow_html=True)

# Handling button clicks
if season1:
    argument = "### 📊 Season 1 Analysis!"
    classes(argument)

if season2:
    argument = "### 📊 Season 2 Analysis!"
    classes(argument)

if season3:
    argument = "### 📊 Season 3 Analysis!"
    classes(argument)
