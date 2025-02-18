import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.express as px
from PIL import Image
import streamlit.components.v1 as components 

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
def sharks():
    pass

  
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

st.markdown("---")
#sharks det
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

st.markdown(f"<h1 style='text-align: center;'>sharks analysis</h1>", unsafe_allow_html=True)


length=len(season1_sharks)
col_list=['col1','col2','col3','col4','col5','col6','col7','col8','col9','col10']
cols = st.columns(len(season1_sharks))  # Creates dynamic columns

for i, col in enumerate(cols):
    with col:
        abc= st.button(season1_sharks[i])




st.markdown("---")
data = {
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Value': [25, 15, 30, 10, 20],
    'Details': [
        {'info': 'Details about category A', 'more': 'Even more info about A'},
        {'info': 'Details about category B', 'more': 'Even more info about B'},
        {'info': 'Details about category C', 'more': 'Even more info about C'},
        {'info': 'Details about category D', 'more': 'Even more info about D'},
        {'info': 'Details about category E', 'more': 'Even more info about E'}
    ]
}

df = pd.DataFrame(data)

# Create the bar chart with Altair
chart = alt.Chart(df).mark_bar().encode(
    x='Category',
    y='Value',
    tooltip=['Category', 'Value']  # Optional: Show tooltip on hover
).interactive() # Make the chart interactive so we can select

# Selection for the bar click
selection = alt.selection_single(
    fields=['Category'],  # Select based on Category
    bind='click',  # Select on click
    nearest=True # Select the nearest bar
)


chart = chart.add_selection(selection)

# Display the chart
st.altair_chart(chart, use_container_width=True)

# Display details based on click
selected_category = st.session_state.get('Category', None) # Access the selected category

if selected_category:
    selected_data = df[df['Category'] == selected_category]
    details = selected_data['Details'].iloc[0] # Access the details dictionary

    st.subheader(f"Details for {selected_category}:")
    st.write(details['info'])
    st.write(details['more'])

elif selected_category is None and 'Category' in st.session_state: #Handles the case where the chart has been interacted with but no category is currently selected.
    st.subheader("Click on a bar to see details.")
else:
    st.subheader("Click on a bar to see details.")

