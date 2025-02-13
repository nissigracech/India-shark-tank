import streamlit as st

# Set page config
st.set_page_config(page_title="Shark Tank India EDA Dashboard", layout="wide")

# Apply custom CSS styles
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
            margin: 5px; /* Reduced margin */
        }

        /* Center buttons in a row with minimal spacing */
        .button-container {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 15px; /* Reduced gap between buttons */
            margin-top: 20px;
        }

    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="title">Shark Tank India EDA Dashboard</h1>', unsafe_allow_html=True)

# Button container
st.markdown('<div class="button-container">', unsafe_allow_html=True)

# Display buttons side by side with reduced spacing
col1, col2, col3 = st.columns([0.1, 0.1, 0.1])  # Reduced column width

with col1:
    if st.button("Season 1", key="season1"):
        st.write("Season 1 analysis!")

with col2:
    if st.button("Season 2", key="season2"):
        st.write("Season 2 analysis!")

with col3:
    if st.button("Season 3", key="season3"):
        st.write("Season 3 analysis!")

st.markdown('</div>', unsafe_allow_html=True)
