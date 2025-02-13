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
        .button-container {
            display: flex;
            justify-content: center; /* Center the buttons */
            gap: 15px;  /* Reduce space between buttons */
            margin-top: 10px;
        }

        .button-container button {
            font-weight: bold;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 8px;
            border: 2px solid #FFD700;
        }

        /* Season 1 Button - Filled Yellow */
        .button-container button:nth-child(1) {
            background-color: #FFD700 !important;
            color: black !important;
        }

        /* Season 2 Button - Blue Outline */
        .button-container button:nth-child(2) {
            background-color: transparent !important;
            color: #00A8E8 !important;
            border: 2px solid #00A8E8 !important;
        }

        /* Season 3 Button - White Outline */
        .button-container button:nth-child(3) {
            background-color: transparent !important;
            color: white !important;
            border: 2px solid white !important;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="title">Season Stats</h1>', unsafe_allow_html=True)

# Create buttons using markdown for alignment
st.markdown(
    """
    <div class="button-container">
        <form action="" method="get">
            <input type="submit" name="season" value="Season 1">
            <input type="submit" name="season" value="Season 2">
            <input type="submit" name="season" value="Season 3">
        </form>
    </div>
    """, unsafe_allow_html=True
)

# Handle button clicks using the updated method
query_params = st.query_params
season_selected = query_params.get("season", None)

if season_selected == "Season 1":
    st.write("Season 1 Analysis!")
elif season_selected == "Season 2":
    st.write("Season 2 Analysis!")
elif season_selected == "Season 3":
    st.write("Season 3 Analysis!")
