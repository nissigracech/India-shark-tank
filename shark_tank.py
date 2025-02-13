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

        /* Style buttons */
        .stButton>button {
            border-radius: 8px;
            font-weight: bold;
            font-size: 16px;
            padding: 8px 16px;
            border: 2px solid #FFD700;
        }

        /* Season 1 Button - Filled Yellow */
        .stButton>button:first-child {
            background-color: #FFD700 !important;
            color: black !important;
        }

        /* Season 2 Button - Blue Outline */
        .stButton>button:nth-child(2) {
            background-color: transparent !important;
            color: #00A8E8 !important;
            border: 2px solid #00A8E8 !important;
        }

        /* Season 3 Button - White Outline */
        .stButton>button:last-child {
            background-color: transparent !important;
            color: white !important;
            border: 2px solid white !important;
        }

        /* Center buttons closely together */
        .button-container {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 10px;  /* Reduce space between buttons */
            margin-top: 10px;
        }

    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="title">Season Stats</h1>', unsafe_allow_html=True)

# Button Container - Using Streamlit for interactivity but styling via CSS
st.markdown('<div class="button-container">', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,1,1])  # Equal spacing for buttons

with col1:
    if st.button("Season 1", key="s1"):
        st.write("Season 1 Analysis!")

with col2:
    if st.button("Season 2", key="s2"):
        st.write("Season 2 Analysis!")

with col3:
    if st.button("Season 3", key="s3"):
        st.write("Season 3 Analysis!")

st.markdown('</div>', unsafe_allow_html=True)
