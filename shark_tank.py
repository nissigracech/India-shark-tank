import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.express as px
from PIL import Image
import streamlit.components.v1 as components 

# Set page config
st.set_page_config(page_title="Shark Tank India", layout="wide")

# Load the pre-processed data
filtered_df = pd.read_csv("filtered_df.csv")
season1_df=filtered_df[filtered_df['Season Number'] == 1]
season2_df=filtered_df[filtered_df['Season Number'] == 2]
season3_df=filtered_df[filtered_df['Season Number'] == 3]

#metric box style
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

main_sharks=['']      
All_sharks=['Namita','Vineeta','Anupam',
                'Aman','Peyush','Ritesh','Amit',
                'Ashneer','Azhar','Ghazal','Deepinder',
                'Radhika','Vikas','Ronnie','Varun']
All_guests=['Ashneer','Azhar','Ghazal','Deepinder',
                'Radhika','Vikas','Ronnie','Varun']
season1_sharks=['Namita','Vineeta','Anupam',
                'Aman','Peyush','Ashneer',
                'Ghazal']
season1_guests=[ 'Ashneer','Ghazal' ]
season2_sharks=['Namita','Vineeta','Anupam',
                'Aman','Peyush','Amit','Vikas']
season2_guests=['Ashneer','Azhar','Ghazal','Deepinder',
                'Radhika','Vikas','Ronnie','Varun']
season3_sharks=['Namita','Vineeta','Anupam',
                'Aman','Peyush','Ritesh','Amit',
                'Azhar','Deepinder','Radhika',
                'Ronnie','Varun']
season3_guests=['Azhar','Ghazal','Deepinder',
                'Radhika','Ronnie','Varun']



        
# seasons data function part1 of the dashboard 
def seasons_data(argument, season_df):
    st.markdown(f"<h1 style='text-align: center;'>{argument}</h1>", unsafe_allow_html=True) 
    total_pitches = season_df["Pitch Number"].nunique()
    total_episodes = season_df["Episode Number"].nunique()
    
    
    # Creating a layout with columns
    col1, col2, col3, col4 = st.columns(4) 
    with col1:
        metric_card("Show Host", season_df['Anchor'].mode()[0],"             ")
    with col2:
        metric_card("Season start Date", season_df['Season Start'].max(),"         ")
    with col3:
        metric_card("Season Last date", season_df['Season End'].min(),"          ")
    with col4:
        metric_card("Number of Episodes",season_df['Episode Number'].nunique(),"      ")
        
            
    col5, col6, col7, col8 = st.columns(4)
    with col5:
        metric_card("Total Pitches", season_df['Pitch Number'].nunique(),"          ")
    with col6:
        metric_card("Total Investment(in crores )",f"₹{season_df['Total Deal Amount'].sum() / 100:.2f} crores","          ")
    with col7:
        metric_card("Startups That Received Offers", season_df['Received Offer'].eq(1).sum(),"        ")
    with col8:
        metric_card("Startups That Accepted Offers", season_df['Accepted Offer'].eq(1).sum(),"        ")
        
    col9, col10, col11, col12 = st.columns(4)
    with col9:
        metric_card("Highest Valuation Given ( in ₹ )", f"₹{season_df['Deal Valuation'].max()/ 100:.2f} crores",season_df.loc[season_df['Deal Valuation'] == season_df['Deal Valuation'].max(), 'Startup Name'].values[0])
    with col10:
        metric_card("Lowest Valuation Given ( in ₹ )", f"₹{season_df['Deal Valuation'].min()/ 100:.2f} crores",season_df.loc[season_df['Deal Valuation'] == season_df[season_df['Deal Valuation'] > 0]['Deal Valuation'].min(), 'Startup Name'].values[0])
    with col11:
        metric_card("Highest Equity Given ( in ₹ )", f"₹{season_df['Total Deal Equity'].max()/ 100:.2f} crores",season_df.loc[season_df['Total Deal Equity'] == season_df['Total Deal Equity'].max(), 'Startup Name'].values[0])
    with col12:
        metric_card("Lowest Equity Given ( in ₹ )", f"₹{season_df['Total Deal Equity'].min()/ 100:.2f} crores",season_df.loc[season_df['Deal Valuation'] == season_df['Total Deal Equity'].min(), 'Startup Name'].values[0])
        

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
            ["All Pitches", "Pitches that Received an Offer","Pitches that not Recieved an offer", "Pitches that Accepted an Offer"],
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
        elif st.session_state.selected_filter == "Pitches that not Recieved an offer":
            industry_counts = season_df[season_df['Received Offer'] != 0]['Industry'].value_counts()


        fig = px.bar(
            x=industry_counts.index,
            y=industry_counts.values,
            labels={'x': 'Industry', 'y': 'Count'},
            title=f"Industry-wise Pitch Count ({option})" 
        )

        fig.update_layout(xaxis_tickangle=-45)
        st.plotly_chart(fig, use_container_width=True)

#sharks data function part2 of the function
def sharks():
    pass

#pitches details function part 3
def pitches_metrics(ses_df ):
    startup_names = ses_df["Startup Name"].dropna().unique().tolist()
    col31, col32, col33,col34, col35,col36,col37=st.columns([1,1,1,1,1,1,1])
    with col34:
        selected_startup = st.selectbox("Select a Startup", options=startup_names, index=None, placeholder="Search and select")
    if not selected_startup and startup_names:  # Check if no startup is selected AND there are startups available
        selected_startup = startup_names[0]   
    if selected_startup:
        selected_startup_data = ses_df[ses_df["Startup Name"] == selected_startup].iloc[0]

        # Section 1
        st.subheader("Pitch & Startup Info")
        col1, col2, col3 = st.columns(3)
        with col1:
            metric_card("Air Date", selected_startup_data["Original Air Date"])
        with col2:
            metric_card("Industry", selected_startup_data["Industry"])
        with col3:
            metric_card("No. of Presenters", str(selected_startup_data["Number of Presenters"]))

        # Section 2
        st.subheader("Pitcher Details")
        col4, col5, col6 = st.columns(3)
        with col4:
            metric_card("Pitchers Avg. Age", selected_startup_data["Pitchers Average Age"])
        with col5:
            metric_card("Pitchers State", selected_startup_data["Pitchers State"])
        with col6:
            metric_card("Original Ask Amount", f"${selected_startup_data['Original Ask Amount']:.2f}K")

        # Section 3
        st.subheader("Offer Details")
        col7, col8, col9 = st.columns(3)
        with col7:
            metric_card("Original Offered Equity", f"{selected_startup_data['Original Offered Equity']:.2f}%")
        with col8:
            metric_card("Valuation Requested", f"${selected_startup_data['Valuation Requested']:.2f}Cr")
        with col9:
            metric_card("Received Offer", "Yes" if selected_startup_data["Received Offer"] == 1 else "No")

        # Section 4
        st.subheader("Deal Outcome")
        col10, col11, col12 = st.columns(3)
        with col10:
            metric_card("Accepted Offer", "Yes" if selected_startup_data["Accepted Offer"] == 1 else "No")
        with col11:
            metric_card("Total Deal Amount", f"${selected_startup_data['Total Deal Amount']:.2f}K")
        with col12:
            metric_card("Total Deal Equity", f"{selected_startup_data['Total Deal Equity']:.2f}%")

        # Section 5
        st.subheader("Deal Valuation & Sharks")
        col13, col14, col15 = st.columns(3)
        with col13:
            metric_card("Deal Valuation", f"${selected_startup_data['Deal Valuation']:.2f}Cr")
        with col14:
            metric_card("No. of Sharks in Deal", str(selected_startup_data["Number of Sharks in Deal"]))
        with col15:
            sharks_in_deal = []
            for shark in ["Aman", "Namita", "Vineeta", "Anupam", "Peyush", "Ritesh", "Amit", "Ashneer", "Azhar", "Ghazal", "Deepinder", "Radhika", "Vikas", "Ronnie", "Varun"]:
                if selected_startup_data.get(f"{shark.lower()}_deal", 0) == 1:
                    sharks_in_deal.append(shark)
            metric_card("Sharks in Deal", ", ".join(sharks_in_deal) if sharks_in_deal else "None")
  
# Custom CSS for Gradient Background
st.markdown("""
    <style>
    /* Full page gradient background */
    body, .stApp {
        background: #292b32 !important;
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
# Creating logo and images
st.image("logo_image.png")   
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


# Initialize session state variables
if "selected_season" not in st.session_state:
    st.session_state.selected_season = 1
if "selected_filter" not in st.session_state:
    st.session_state.selected_filter = "All Pitches"

 
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
    seasons_data(argument, season_df)
    st.markdown("---")
    #pitches_metrics(season_df)
elif st.session_state.selected_season == 2:
    argument = "  📊 Season 2 Analysis!"
    season_df = filtered_df[filtered_df['Season Number'] == 2]
    season_df.drop(columns=['Ritesh Present', 'Ritesh_deal'], inplace=True)
    seasons_data(argument, season_df)
    st.markdown("---")
    #pitches_metrics(season_df)
elif st.session_state.selected_season == 3:
    argument = "  📊 Season 3 Analysis!"
    season_df = filtered_df[filtered_df['Season Number'] == 3]
    seasons_data(argument, season_df)
    st.markdown("---")
    #pitches_metrics(season_df)
else:
    argument = "  📊 Season 1 Analysis!"
    season_df = filtered_df[filtered_df['Season Number'] == 1]
    season_df.drop(columns=['Ritesh Present', 'Amit Present', 'Ritesh_deal', 'Amit_deal'], inplace=True)
    seasons_data(argument, season_df)
    st.markdown("---")
    #pitches_metrics(season_df)
    
 
#-----------------------------------------------------------------------------------------------
  
st.markdown(f"<h1 style='text-align: center;'>sharks analysis</h1>", unsafe_allow_html=True)

col_list=['col1','col2','col3','col4','col5','col6','col7','col8','col9','col10']
cols = st.columns(len(season1_sharks))  # Creates dynamic columns

for i, col in enumerate(cols):
    with col:
        abc= st.button(season1_sharks[i])


season1_df=filtered_df[filtered_df['Season Number'] == 1]

st.markdown("---")
 
 
 

shark_columns = [
    "Namita", "Vineeta", "Anupam", "Aman", "Peyush", "Ritesh", "Amit"  # ... other sharks
]

shark_deal_counts = {}
 
    
    

 
 
if st.session_state.selected_season == 1: 
    pitches_metrics(season1_df)
elif st.session_state.selected_season == 2: 
    pitches_metrics(season2_df)
elif st.session_state.selected_season == 3: 
    pitches_metrics(season3_df)
else:
    pitches_metrics(season1_df)