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

        /* Centered button container */
        .button-container {
            display: flex;
            justify-content: center;
            gap: 15px;  /* Reduce space between buttons */
            margin-top: 10px;
        }

        /* Styled buttons */
        .custom-button {
            font-weight: bold;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 8px;
            border: 2px solid #FFD700;
            cursor: pointer;
            display: inline-block;
            text-align: center;
            text-decoration: none;
        }

        /* Season 1 Button - Filled Yellow */
        .season1 {
            background-color: #FFD700 !important;
            color: black !important;
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

# Creating a horizontal button layout using markdown
st.markdown("""
    <div class="button-container">
        <a href="?season=1" class="custom-button season1">Season 1</a>
        <a href="?season=2" class="custom-button season2">Season 2</a>
        <a href="?season=3" class="custom-button season3">Season 3</a>
    </div>
""", unsafe_allow_html=True)

# Handling button clicks
query_params = st.query_params
selected_season = query_params.get("season", None)

if selected_season:
    st.write(f"### Season {selected_season} Analysis!")
