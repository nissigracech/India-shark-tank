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
col1, col2, col3 = st.columns([4,1, 15])  

with col1:
    st.image("stilogo.png", caption=" ", width=400)  # Smaller Image

with col3:
    st.image("st.png", caption=" ", width=1000)  # Larger Image


 
st.image("abc.png")  # Smaller Image

 

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


st.markdown(f"<h1 style='text-align: center;'>sharks analysis</h1>", unsafe_allow_html=True)


length=len(season1_sharks)
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

for shark in shark_columns:
    deal_column = f"{shark}_deal"  # The binary deal column (0 or 1)
    if deal_column in season1_df.columns:
        shark_deal_counts[shark] = season1_df[deal_column].sum()  # Sum directly (1s and 0s)
    else:
        print(f"Warning: Column '{deal_column}' not found. Skipping.")
        shark_deal_counts[shark] = 0

shark_data = pd.DataFrame(list(shark_deal_counts.items()), columns=['Shark', 'Deal Count'])

# --- Plotting with Matplotlib (only Deal Count) ---
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(shark_data['Shark'], shark_data['Deal Count'], color='skyblue')
ax.set_xlabel("Shark")
ax.set_ylabel("Deal Count")
ax.set_title("Number of Deals per Shark")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
st.pyplot(fig)


# --- Detailed Information on Click ---

def show_details(selected_shark):
    st.subheader(f"Deals by {selected_shark}:")
    deal_column = f"{selected_shark}_deal"
    invested_pitches = season1_df[season1_df[deal_column] == 1]  # Filter where the deal column is 1

    if not invested_pitches.empty:
        st.dataframe(invested_pitches[[
            "Startup Name", "Industry", "Original Ask Amount", "Total Deal Amount", "Deal Valuation" #Add more columns as needed
        ]])
    else:
        st.write(f"{selected_shark} did not participate in any deals.")

selected_shark = st.selectbox("Select a Shark", shark_data['Shark'].tolist())

if selected_shark:
    show_details(selected_shark)
    
    
    
    


import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Sample Data
sharks = ["Aman", "Namita", "Vineeta", "Anupam", "Peyush"]
pitches = [10, 15, 20, 8, 12]

# Create figure
fig, ax = plt.subplots(figsize=(10, 5))

# Set background color
fig.patch.set_facecolor('#2C3E50')  # Dark blue-gray background
ax.set_facecolor('#D6EAF8')  # Light blue background inside plot

# Create bar plot
sns.barplot(x=sharks, y=pitches, palette="coolwarm", ax=ax)

# Change title color
ax.set_title("Number of Pitches Invested Per Shark", fontsize=14, color='black')

# Customize tick labels color
ax.tick_params(colors='black')

# Remove border lines to blend with background
for spine in ax.spines.values():
    spine.set_visible(False)

# Show plot in Streamlit
st.pyplot(fig)
