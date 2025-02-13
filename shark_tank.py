import streamlit as st

# Set page config
st.set_page_config(page_title="Shark Tank India EDA Dashboard", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        /* Centered bold uppercase yellow title */
        .title {
            text-align: center;
            font-weight: 900;
            font-size: 3em;
            color: #FFD700; /* Gold Yellow */
            text-transform: uppercase;
        }

        /* Sidebar background gradient */
        [data-testid="stSidebar"] {
            background: linear-gradient(135deg, #050A13, #0B132B, #1B263B, #415A77) !important;
            color: white;
        }

        /* Sidebar text styling */
        [data-testid="stSidebar"] * {
            color: white !important;
            font-weight: bold;
        }

        /* Button styling */
        .custom-button {
            width: 200px;
            font-weight: bold;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 8px;
            border: 2px solid transparent;
            cursor: pointer;
            text-align: center;
            display: block;
            margin: 10px auto; /* Centers buttons inside column */
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
st.markdown('<h1 class="title">Season Stats</h1>', unsafe_allow_html=True)

# Create 3 columns (Left empty, Center with buttons, Right empty)
col1, col2, col3 = st.columns([1, 2, 1])  # Adjust width to center buttons

with col2:
    st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)

    season1 = st.button("Season 1", key="s1")
    season2 = st.button("Season 2", key="s2")
    season3 = st.button("Season 3", key="s3")

    st.markdown('</div>', unsafe_allow_html=True)

# Handling button clicks
if season1:
    st.write("### 📊 Season 1 Analysis!")

if season2:
    st.write("### 📊 Season 2 Analysis!")

if season3:
    st.write("### 📊 Season 3 Analysis!")
