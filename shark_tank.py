import streamlit as st
import pandas as pd
import plotly.express as px
from PIL import Image  # If you're still using images
import streamlit.components.v1 as components  # If needed
import base64

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
    total_pitches = season_df["Pitch Number"].nunique()
    total_episodes = season_df["Episode Number"].nunique()
    st.markdown(
    """
    <style>
    .metric-card {
        background-color: #161616;
        padding: 50px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0px 2px 4px rgba(255, 255, 255, 0.1);
        margin-bottom: 20px;
    }
    .metric-title {
        font-size: 18px;
        color: #bbb;
    }
    .metric-value {
        font-size: 32px;
        font-weight: bold;
        color: #FFD700; /* Gold color */
    }
    .metric-subtitle {
        font-size: 16px;
        color: #888;
        margin-top: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    # Function to create metric cards
    def metric_card(title, value, subtitle=""):
        st.markdown(
        f"""
        <div class="metric-card">
            <div class="metric-title">{title}</div>
            <div class="metric-value">{value}</div>
            {f'<div class="metric-subtitle">{subtitle}</div>' if subtitle else ''}
        </div>
        """,
        unsafe_allow_html=True
        )
    
    # Creating a layout with columns
    col1, col2, col3, col4 = st.columns(4) 
    with col1:
        metric_card("Show Host", season_df['Anchor'].mode()[0]," ")
    with col2:
        metric_card("Season start Date", season_df['Season Start'].max()," ")
    with col3:
        metric_card("Season Last date", season_df['Season End'].min()," ")
    with col4:
        metric_card("Number of Episodes",season_df['Episode Number'].nunique()," ")
        
            
    col5, col6, col7, col8 = st.columns(4)
    with col5:
        metric_card("Total Pitches", season_df['Pitch Number'].nunique()," ")
    with col6:
        metric_card("Total Investment(in crores )",f"₹{season_df['Total Deal Amount'].sum() / 100:.2f} crores"," ")
    with col7:
        metric_card("Startups That Received Offers", season_df['Received Offer'].eq(1).sum()," ")
    with col8:
        metric_card("Startups That Accepted Offers", season_df['Accepted Offer'].eq(1).sum()," ")
        
    col9, col10, col11, col12 = st.columns(4)
    with col9:
        metric_card("Total Pitches", season_df['Pitch Number'].nunique()," ")
    with col10:
        metric_card("Total Investment(in crores )",f"₹{season_df['Total Deal Amount'].sum() / 100:.2f} crores"," ")
    with col11:
        metric_card("Startups That Received Offers", season_df['Received Offer'].eq(1).sum()," ")
    with col12:
        metric_card("Startups That Accepted Offers", season_df['Accepted Offer'].eq(1).sum()," ")
        

    col20, col22 = st.columns(2)
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
            key="filter_selectbox" 
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
            title=f"Industry-wise Pitch Count ({option})" 
        )

        fig.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)
def sharks():
    pass

import streamlit as st
import base64

# Function to encode a local image to Base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        base64_str = base64.b64encode(img_file.read()).decode()
    return f"data:image/png;base64,{base64_str}"

# Paths to your local images
image_path = "background.jpg"  # Change this to your image filename

# Get base64 encoded image
encoded_image = get_base64_image(image_path)

# Custom CSS for top and bottom background
st.markdown(
    f"""
    <style>
    .top-bg {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 20%; /* Adjust height */
        background-image: url("{encoded_image}");
        background-size: cover;
        background-position: center;
        z-index: -1;
    }}

    .bottom-bg {{
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        height: 20%; /* Adjust height */
        background-image: url("{encoded_image}");
        background-size: cover;
        background-position: center;
        z-index: -1;
    }}

    .middle-section {{
        background-color: #f5f5f5; /* Light grey middle */
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }}
    </style>
    <div class="top-bg"></div>
    <div class="bottom-bg"></div>
    """,
    unsafe_allow_html=True
)

# Streamlit layout
st.title("Shark Tank India Dashboard")

st.markdown('<div class="middle-section">', unsafe_allow_html=True)
st.subheader("Main Content in the Middle")
st.write("This section has a different background color, separating it from the top and bottom images.")
st.markdown('</div>', unsafe_allow_html=True)

  
 

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

st.markdown("---")
#sharks details
