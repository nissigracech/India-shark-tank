import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import plotly
from PIL import Image
import streamlit.components.v1 as components  


# Set page config
st.set_page_config(page_title="Shark Tank India EDA Dashboard", layout="wide")

df=pd.read_csv("Shark Tank India.csv")

df = df[df['Episode Title'] != 'Unseen']

df['Aman_deal'] = df['Aman Investment Amount'].map(lambda x: 1 if isinstance(x, (int, float)) and not pd.isna(x) else 0)
df['Namita_deal'] = df['Namita Investment Amount'].map(lambda x: 1 if isinstance(x, (int, float)) and not pd.isna(x) else 0)
df['Vineeta_deal'] = df['Vineeta Investment Amount'].map(lambda x: 1 if isinstance(x, (int, float)) and not pd.isna(x) else 0)
df['Anupam_deal'] = df['Anupam Investment Amount'].map(lambda x: 1 if isinstance(x, (int, float)) and not pd.isna(x) else 0)
df['peyush_deal'] = df['Peyush Investment Amount'].map(lambda x: 1 if isinstance(x, (int, float)) and not pd.isna(x) else 0)
df['Ritesh_deal'] = df['Ritesh Investment Amount'].map(lambda x: 1 if isinstance(x, (int, float)) and not pd.isna(x) else 0)
df['Amit_deal'] = df['Amit Investment Amount'].map(lambda x: 1 if isinstance(x, (int, float)) and not pd.isna(x) else 0)


df['deal_amount_per_shark']=df['Total Deal Amount']/df['Number of Sharks in Deal']
df['equity_per_shark']=df['Total Deal Equity']/df['Number of Sharks in Deal']


df['Boot Strapped']=df['Bootstrapped'].map(lambda x: 1 if x in ['yes', 'funded'] else 0)
df.drop('Bootstrapped' , axis=1, inplace=True)
df['Pitchers State']=df['Pitchers State'].fillna(df['Pitchers State'].mode()[0])

general_info=['Season Number', 'Startup Name',
              'Episode Number', 'Pitch Number',
              'Episode Title','Anchor', 'Industry',
              'Number of Presenters','Pitchers Average Age',
              'Original Ask Amount', 'Original Offered Equity',
              'Valuation Requested', 'Received Offer', 'Accepted Offer',
              'Total Deal Amount', 'Total Deal Equity',  'Deal Valuation', 
              'Number of Sharks in Deal','Pitchers State',
              'Boot Strapped']


time_details=['Season Start', 'Season End', 'Original Air Date']

pitchers_business_details=['Business Description','Company Website',
                           'Started in', 'Male Presenters',
                           'Female Presenters', 'Transgender Presenters', 
                           'Couple Presenters','Pitchers City']

brand_renvue_details=['Yearly Revenue', 'Monthly Sales', 
                      'Gross Margin', 'Net Margin',
                      'EBITDA', 'Cash Burn',
                      'SKUs', 'Has Patents','Part of Match off']

more_into_pitching_brands=['Deal Has Conditions', 'Royalty Percentage', 
                           'Royalty Recouped Amount','Advisory Shares Equity']

sharks_presence=['Namita Present', 
                 'Vineeta Present', 'Anupam Present',
                 'Aman Present','Peyush Present',
                 'Ritesh Present', 'Amit Present', 'Guest Present']

Debt_details=['Total Deal Debt','Debt Interest','Namita Debt Amount', 'Vineeta Debt Amount','Anupam Debt Amount','Aman Debt Amount', 'Peyush Debt Amount',
               'Ritesh Debt Amount', 'Amit Debt Amount','Guest Debt Amount']

sharks_ivestment_equity_details=['Namita Investment Amount','Namita Investment Equity',  
                                 'Vineeta Investment Amount', 'Vineeta Investment Equity', 
                                 'Anupam Investment Amount','Anupam Investment Equity',  
                                 'Aman Investment Amount', 'Aman Investment Equity',  
                                 'Peyush Investment Amount', 'Peyush Investment Equity', 
                                 'Ritesh Investment Amount', 'Ritesh Investment Equity',  
                                 'Amit Investment Amount', 'Amit Investment Equity',  
                                 'Guest Investment Amount', 'Guest Investment Equity']

guest_related=['All Guest Names','Invested Guest Name','']


removing_col=brand_renvue_details+pitchers_business_details+sharks_ivestment_equity_details+Debt_details+more_into_pitching_brands
filtered_df=df.drop(columns=removing_col)

#guest details 
Guest_list=['Ashneer Grover','Azhar Iqubal','Ghazal Alagh',
            'Deepinder Goyal','Radhika Gupta','Vikas D Nahar',
            'Ronnie Screwvala','Varun Dua']
guest_list_short_cut=['Ashneer','Azhar','Ghazal',
            'Deepinder','Radhika','Vikas',
            'Ronnie','Varun']

#creating new columns for guest present and deals
j=0
k=0
for i in Guest_list:
    new_col=guest_list_short_cut[j]+'_present'
    filtered_df[new_col]=filtered_df['All Guest Names'].apply(lambda x: 1 if pd.notna(x) and i in x else 0)
    filtered_df[new_col] = filtered_df['All Guest Names'].apply(lambda x: 1 if pd.notna(x) and i in x else 0)
    filtered_df['All Guest Names'] = filtered_df['All Guest Names'].apply(lambda x: x.replace(i, '').strip() if pd.notna(x) else x)
    filtered_df['All Guest Names'] = filtered_df['All Guest Names'].apply(lambda x: x.replace(i, '').strip() if pd.notna(x) else x)
    j+=1


for i in Guest_list:
    new_col=guest_list_short_cut[k]+'_deal'
    filtered_df[new_col]=filtered_df['Invested Guest Name'].apply(lambda x: 1 if pd.notna(x) and i in x else 0)
    filtered_df[new_col] = filtered_df['Invested Guest Name'].apply(lambda x: 1 if pd.notna(x) and i in x else 0)
    filtered_df['All Guest Names'] = filtered_df['All Guest Names'].apply(lambda x: x.replace(i, '').strip() if pd.notna(x) else x)
    filtered_df['All Guest Names'] = filtered_df['All Guest Names'].apply(lambda x: x.replace(i, '').strip() if pd.notna(x) else x)
    k+=1


# data handling
# missing values
filtered_df['Accepted Offer']=filtered_df['Accepted Offer'].fillna(-1)
filtered_df['Accepted Offer']=filtered_df['Accepted Offer'].astype('int64')
filtered_df['Number of Sharks in Deal']=filtered_df['Number of Sharks in Deal'].fillna(0)
filtered_df['Number of Sharks in Deal']=filtered_df['Number of Sharks in Deal'].astype('int64')
for i in sharks_presence:
    filtered_df[i]=filtered_df[i].fillna(0)
    filtered_df[i]=filtered_df[i].astype('int64')
    

filtered_df['Total Deal Amount']=filtered_df['Total Deal Amount'].fillna(0)
filtered_df['Total Deal Equity']=filtered_df['Total Deal Equity'].fillna(0)
filtered_df['Deal Valuation']=filtered_df['Deal Valuation'].fillna(0)
filtered_df['deal_amount_per_shark']=filtered_df['deal_amount_per_shark'].fillna(0)
filtered_df['equity_per_shark']=filtered_df['equity_per_shark'].fillna(0)




def classes(argument,season_df):
    st.markdown(f"<h1 style='text-align: center;'>{argument}</h1>", unsafe_allow_html=True)
    total_pitches = season_df["Pitch Number"].nunique()
    total_episodes = season_df["Episode Number"].nunique()
    st.write(season_df["Episode Number"].nunique())
    st.write(season_df.columns)



    

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

#--------------------------------------------------------------------------------------------------

st.markdown("---")  

#-------------------------------------------------------------------------------------------------
# creating buttons for seasons 
# Create 3 main columns (Left empty, Center with buttons, Right empty)
col1, col2, col3 = st.columns([1, 2, 1])  # Adjust width to center buttons

with col2:
    # Create another row of columns inside col2 for buttons
    sub_col1, sub_col2, sub_col3,sub_col4,sub_col5,sub_col6,sub_col7 = st.columns([4, 10, 3, 10, 3, 10, 2])  # Equal width columns

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

# Handling button clicks
if season1:
    argument = "  📊 Season 1 Analysis!"
    season1_df=filtered_df[filtered_df['Season Number']==1]
    season1_df.drop(columns=['Ritesh Present', 'Amit Present','Ritesh_deal','Amit_deal'],inplace=True)
    classes(argument,season1_df)
    

if season2:
    argument = "  📊 Season 2 Analysis!"
    season2_df=filtered_df[filtered_df['Season Number']==2]
    season2_df.drop(columns=['Ritesh Present' ,'Ritesh_deal' ],inplace=True)
    classes(argument,season2_df)

if season3:
    argument = "  📊 Season 3 Analysis!"
    season3_df=filtered_df[filtered_df['Season Number']==3]
    classes(argument,season3_df)




