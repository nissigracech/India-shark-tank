import streamlit as st

# Set page config
st.set_page_config(page_title="Shark Tank India EDA Dashboard", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
        /* Centered bold title */
        .title {
            text-align: center;
            font-weight: bold;
            font-size: 2em;
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

        /* Style dropdowns, sliders, and input boxes */
        select, input, .stSlider, .stMultiSelect {
            background-color: rgba(255, 255, 255, 0.15) !important;
            color: white !important;
            border-radius: 8px;
            padding: 8px;
            border: 1px solid rgba(255, 255, 255, 0.3);
        }

        /* Style buttons */
        .stButton>button {
            background-color: #00509E !important;
            color: white !important;
            border-radius: 8px;
            font-weight: bold;
            padding: 10px 20px;
            border: none;
            cursor: pointer;
        }

        /* Center buttons closely together */
        .button-container {
            display: flex;
            padding: 10px 20px;
            justify-content: center;
            align-items: center;
            gap: 0px;  /* REDUCE SPACE BETWEEN BUTTONS */
            margin-top: 20px;
        }

    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="title">Shark Tank India EDA Dashboard</h1>', unsafe_allow_html=True)

# Button Container - Using HTML for precise positioning
st.markdown('<div class="button-container">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3, gap="small")  # Reduce column spacing

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
