import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image  # If you're still using images
import streamlit.components.v1 as components  # If needed

# Set page config
st.set_page_config(page_title="Shark Tank India EDA Dashboard", layout="wide")

# Load the pre-processed data
filtered_df = pd.read_csv("filtered_df.csv")

# Initialize session state variables
if "selected_season" not in st.session_state:
    st.session_state.selected_season = 1
if "selected_filter" not in st.session_state:
    st.session_state.selected_filter = "All Pitches"


def classes(argument, season_df):
    st.markdown(f"<h1 style='text-align: center;'>{argument}</h1>", unsafe_allow_html=True)

    # Metric Cards (Your existing code)
    # ...

    col20, col22 = st.columns(2)
    with col20:
        st.subheader("Industry-wise Pitch Count")
        industry_counts = season_df['Industry'].value_counts()
        fig = px.bar(
            x=industry_counts.index,
            y=industry_counts.values,
            labels={'x': 'Industry', 'y': 'Count'},
            title="Industry-wise Pitch Count"
        )
        fig.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)

    with col22:
        # Scoped CSS for dropdown width
        st.markdown(
            """
            <style>
            div[data-baseweb="select"] > div {
            width: 200px !important;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        option = st.selectbox(
            "Select Pitch Perspective",
            ["All Pitches", "Pitches that Received an Offer", "Pitches that Accepted an Offer"],
            key="filter_selectbox",
            on_change=update_filter
        )
        st.session_state.selected_filter = option


        def update_filter():
            st.session_state.selected_filter = st.session_state.filter_selectbox
            st.experimental_rerun()  # Force Streamlit to re-run

        # Filtering data based on selection (using session state)
        if st.session_state.selected_filter == "All Pitches":
            industry_counts = season_df['Industry'].value_counts()
        elif st.session_state.selected_filter == "Pitches that Received an Offer":
            industry_counts = season_df[season_df['Received Offer'] == 1]['Industry'].value_counts()
        elif st.session_state.selected_filter == "Pitches that Accepted an Offer":
            industry_counts = season_df[season_df['Accepted Offer'] == 1]['Industry'].value_counts()


        fig = px.bar(
            x=industry_counts.index,
            y=industry_counts.values,
            labels={'x': 'Industry', 'y': 'Count'},
            title=f"Industry-wise Pitch Count ({option})",
            color=industry_counts.values,
            color_continuous_scale="viridis"
        )

        fig.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)


# Custom CSS for styling (Your existing code)
st.markdown(
    """
    <style>
    /* ... (Your CSS) ... */
    </style>
    """,
    unsafe_allow_html=True,
)

# Logo and Image display (Your existing code)
# ...
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
            width: 180px;
            font-weight: bold;
            font-size: 32px;
            padding: 18px;
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

#-------------------------------------------------------------------------------
# creating logo and image 
col1, col2, col3 = st.columns([4,1, 15])  

with col1:
    st.image("stilogo.png", caption=" " , width=400)  # Smaller Image

with col3:
    st.image("st.png", caption=" ", width=1000)  # Larger Image

st.markdown("---")

# Season selection buttons
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    sub_col1, sub_col2, sub_col3, sub_col4, sub_col5, sub_col6, sub_col7 = st.columns(
        [4, 10, 3, 10, 3, 10, 2]
    )

    with sub_col2:
        st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
        season1 = st.button("Season 1", key="s1")
        st.markdown("</div>", unsafe_allow_html=True)

    with sub_col4:
        st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
        season2 = st.button("Season 2", key="s2")
        st.markdown("</div>", unsafe_allow_html=True)

    with sub_col6:
        st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
        season3 = st.button("Season 3", key="s3")
        st.markdown("</div>", unsafe_allow_html=True)


# Handling button clicks (using session state)
if season1:
    st.session_state.selected_season = 1
elif season2:
    st.session_state.selected_season = 2
elif season3:
    st.session_state.selected_season = 3

# Displaying the correct season (using session state)
if st.session_state.selected_season == 1:
    argument = "  📊 Season 1 Analysis!"
    season_df = filtered_df[filtered_df['Season Number'] == 1]
    season_df.drop(columns=['Ritesh Present', 'Amit Present', 'Ritesh_deal', 'Amit_deal'], inplace=True)
    classes(argument, season_df)
elif st.session_state.selected_season == 2:
    argument = "  📊 Season 2 Analysis!"
    season_df = filtered_df[filtered_df['Season Number'] == 2]
    season_df.drop(columns=['Ritesh Present', 'Ritesh_deal'], inplace=True)
    classes(argument, season_df)
elif st.session_state.selected_season == 3:
    argument = "  📊 Season 3 Analysis!"
    season_df = filtered_df[filtered_df['Season Number'] == 3]
    classes(argument, season_df)


# Default display (if no button clicked initially) - Not strictly needed now
# but kept for completeness
# if "selected_season" not in st.session_state: # No longer really needed
#     argument = "  📊 Season 1 Analysis!"
#     season_df = filtered_df[filtered_df['Season Number'] == 1]
#     season_df.drop(columns=['Ritesh Present', 'Amit Present', 'Ritesh_deal', 'Amit_deal'], inplace=True)
#     classes(argument, season_df)