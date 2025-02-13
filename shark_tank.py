import streamlit as st

# Set page config
st.set_page_config(page_title="Shark Tank India EDA Dashboard", layout="wide")

# Centered bold title
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
            margin: 10px;
        }

        /* Center the buttons */
        .button-container {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 20px;
        }

    </style>
""", unsafe_allow_html=True)


# Create three buttons below the title
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Season 1"):
        st.write("season 1 analysis!")

with col2:
    if st.button("Season 2"):
        st.write("season 2 analysis Analysis!")

with col3:
    if st.button("Season 3"):
        st.write("season 3 analysis")
