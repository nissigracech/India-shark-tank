import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.express as px  

# Set page config
st.set_page_config(page_title="Shark Tank India", layout="wide")

# Load the pre-processed data
try:
    filtered_df = pd.read_csv("filtered_df.csv")
except FileNotFoundError:
    st.error("Error: filtered_df.csv not found. Please upload the file.")
    st.stop()  # Stop execution if file is missing
except pd.errors.ParserError:  # Catch CSV parsing errors
    st.error("Error: Could not parse filtered_df.csv. Check the file format.")
    st.stop()
except Exception as e: # Catch other potential errors
    st.error(f"An unexpected error occurred: {e}")
    st.stop()

# categorise the data for each season
season1_df=filtered_df[filtered_df['Season Number'] == 1]
season1_df.drop(columns=['Ritesh Present', 'Ritesh Deal', 
                         'Amit Present','Amit Deal',
                         'Azhar Present','Azhar Deal',
                         'Deepinder Present','Deepinder Deal',
                         'Radhika Present','Radhika Deal',
                         'Vikas Present','Vikas Deal',
                         'Ronnie Present','Ronnie Deal',
                         'Varun Present','Varun Deal'], inplace=True)
season2_df=filtered_df[filtered_df['Season Number'] == 2]
season2_df.drop(columns=['Ritesh Present', 'Ritesh Deal',
                         'Ashneer Present','Ashneer Deal',
                         'Azhar Present','Azhar Deal',
                         'Ghazal Present','Ghazal Deal',
                         'Deepinder Present','Deepinder Deal',
                         'Radhika Present','Radhika Deal',
                         'Ronnie Present','Ronnie Deal',
                         'Varun Present','Varun Deal'], inplace=True)
season3_df=filtered_df[filtered_df['Season Number'] == 3]
season3_df.drop(columns=[ 'Ashneer Present','Ashneer Deal',
                          'Ghazal Present','Ghazal Deal',
                          'Vikas Present','Vikas Deal' ],inplace=True)

st.session_state.selected_guest_shark=""
st.session_state.selected_guest_shark_filter=""
def guest_selection(guest_list):
    if "selected_guest_shark" not in st.session_state:
        st.session_state.selected_guest_shark=guest_list[0]
        st.session_state.selected_guest_shark_filter=guest_list[0]
        

# Initialize session state variables
if "selected_season" not in st.session_state:
    st.session_state.selected_season = 1
if "selected_filter" not in st.session_state:
    st.session_state.selected_filter = "All Pitches"
if "selected_shark" not in st.session_state:
    st.session_state.selected_shark="Namita"
    

 

# metric box style for metric cards of all sections 
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
        color: #fbdf71; /* Gold color */
    }
    .metric-subtitle {
        font-size: 16px;
        color: #888;
        margin-top: 5px;
    }
    
    #shark metric card
    .shark_metric-card {
        background-color: #161616;
        padding: 20px; /* Reduced padding */
        border-radius: 10px;
        text-align: center;
        box-shadow: 0px 2px 4px rgba(255, 255, 255, 0.1);
        margin-bottom: 20px;
        width: 100%; /* Make card fill column width */
        height: 300px
        box-sizing: border-box; /* Include padding and border in element's total width and height */
    }
    .shark_metric-title {
        font-size: 40px; /* Increased name size */
        font-weight: bold; /* Name more prominent */
        color: #FFD700; /* Gold color for name */
    }
    .shark_metric-value {
        font-size: 26px; /* Slightly smaller occupation */
        color: #bbb; /* Less bright color for occupation */
        font-weight: bold;
    }
    .shark_metric-subtitle {
        font-size: 20px; /* Education size */
        color: #888; /* Education color */
        margin-top: 5px;
        font-weight: bold;
    }
    .column-spacer {
        width: 2%; /* Adjust spacing between columns */
    }
    </style>
    """,
    unsafe_allow_html=True
)
# Function to create metric cards for season,sharks info and pitches 
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
# Function to create metric cards for sharks images
def shark_info_metric_card(name, occupation, education):
    space=" "
    st.markdown(
        f"""
        <div class="shark_metric-card"> 
            <div class="shark_metric-title">&nbsp;</div> 
            <div class="shark_metric-title">{name}</div> 
            <div class="shark_metric-value">{occupation}</div> 
            {f'<div class="metric-subtitle">Education:{education}</div>' if education else ''} 
        </div>
        """,
        unsafe_allow_html=True
    )
 
main_sharks=['Namita','Vineeta','Anupam','Aman','Peyush']      
All_sharks=['Namita','Vineeta','Anupam','Aman','Peyush','Ritesh','Amit',
                'Ashneer','Azhar','Ghazal','Deepinder','Radhika','Vikas','Ronnie','Varun']
main_sharks=['Namita','Vineeta','Anupam','Aman','Peyush']
All_guests=['Ritesh','Amit','Ashneer','Azhar','Ghazal','Deepinder','Radhika','Vikas','Ronnie','Varun']
season1_sharks=['Namita','Vineeta','Anupam','Aman','Peyush','Ashneer','Ghazal']
season1_guests=[ 'Ashneer','Ghazal' ]
season2_sharks=['Namita','Vineeta','Anupam','Aman','Peyush','Amit','Vikas']
season2_guests=[ 'Amit','Vikas' ]
season3_sharks=['Namita','Vineeta','Anupam','Aman','Peyush','Ritesh','Amit',
                'Azhar','Deepinder','Radhika','Ronnie','Varun']
season3_guests=['Ritesh','Amit','Azhar','Deepinder', 'Radhika','Ronnie','Varun']

def count_shark_presence(data, shark_names):
    presence_counts = {}
    for shark_name in shark_names:
        present_column = f"{shark_name} Present"
        if present_column in data.columns:
             presence_counts[shark_name]=data[present_column].sum() 
    return presence_counts

def count_shark_deal(data, shark_names):
    deal_counts = {}
    for shark_name in shark_names:
        deal_column = f"{shark_name} Deal"
        if deal_column in data.columns:
             deal_counts[shark_name]=data[deal_column].sum() 
    return deal_counts

def count_shark_deal_amount(data,shark_names):
    shark_deal_amount={}
    for shark_name in shark_names:
        deal=shark_name+" Deal" 
        shark_deal_amount[shark_name]=data[data[deal] == 1]["deal_amount_per_shark"].sum()/100
    return shark_deal_amount
    
def sharks_info(season_df,keys,shark_name, occupation, education,guest_list):
    if st.session_state.selected_shark == "Guests": 
        guest_selection(guest_list)
        if st.session_state.selected_season == 0:
            season = "overall"
        else:
            season = "season" + str(st.session_state.selected_season)  # Important: Convert to string!
        st.markdown(f"<h2 style='text-align: center;font-size: 18px;color: #bbb'>Guest present in {season} are {",".join(guest_list)}</h2>", unsafe_allow_html=True)
        col700,col701,col703,col704,col705=st.columns([5, 5, 3, 5, 5])
        st.markdown(
        """
        <style>
        div[data-baseweb="select"] > div {  /* Target the selectbox container */
            width: 200px !important;  /* Set desired width */
        }
        div[data-baseweb="select"] > div > div { /* Target the inner container */
            font-size: 20px !important; /* Set desired font size */
            height: 50px !important; /* Set a larger height */
        }
        div[data-baseweb="select"] > div > div > div { /* Target the dropdown list */
            font-size: 20px !important; /* Set desired font size */
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
        with col703: 
            option = st.selectbox("Select Shark(guest) Name:", guest_list, index=0)  
        keys=option
        
    else:
        image_info="Images/"+keys+".jpg"
        col400,col401,col402,col403=st.columns([3,4,7,3])
        with col401:
            st.image(image_info,width=300)
        with col402:
            shark_info_metric_card(shark_name,occupation,education)
        
    
    # begin of shark metric cards
    #section 1
    deal=keys+" Deal"
    present=keys+" Present"
    #key_df=season_df[deal==1]
    col416,col417,col418,col419,col420=st.columns([1,3,3,3,1])
    with col417:
        metric_card("Present in no.of pitches",season_df[present].sum(),"")
        pass
    with col418:
        metric_card("Number of deals done ",season_df[deal].sum(),"")
    with col419:
        metric_card("Total Invested Amount",f'₹{season_df[season_df[deal] == 1]["deal_amount_per_shark"].sum()/100:.2f} Cr',"")
        
    # sections 2
    col411,col412, col413,col414,col415=st.columns([1,3,3,3,1])
    key_deals = season_df[season_df[deal] == 1]
    key_deals["Valuation"] = (key_deals["deal_amount_per_shark"] / key_deals["equity_per_shark"]) * 100
    with col412: 
        metric_card("Highest Deal amount",
                    f'₹{key_deals['deal_amount_per_shark'].max()/100:.2f}Cr',
                    key_deals.loc[key_deals['deal_amount_per_shark']==key_deals['deal_amount_per_shark'].max(),'Startup Name'].values[0])
    with col413:
        metric_card("Highest Deal valuation",
                    f'₹{key_deals['Valuation'].max()/100:.2f}Cr',
                    key_deals.loc[key_deals['Valuation']==key_deals['Valuation'].max(),'Startup Name'].values[0])
    with col414:
        metric_card("Number of solo investments",len(season_df[(season_df[deal] == 1) & (season_df["Number of Sharks in Deal"] == 1)]))
    
    # bar graph
    fig = px.line(key_deals, x='Startup Name', y=['Total Deal Amount', 'deal_amount_per_shark', 'Original Ask Amount'], 
                  title='Multiline Chart of b, c, and d vs. a',
                  labels={'value': 'Values', 'variable': 'Column'},
                  markers=True,  # Add markers for each point
                color_discrete_map={
            "Total Deal Amount": "red",
            "deal_amount_per_shark": "blue",
            "Original Ask Amount": "green"
        })
    fig.update_layout(xaxis_title="Column a (Categories)", yaxis_title="Values")
    st.plotly_chart(fig)

# seasons data function part1 of the dashboard 
def seasons_data(argument, season_df,season_sharks):
    st.markdown(f"<h1 style='text-align: center;font-family: \"Times New Roman\", serif; color: #FFD700;'>{argument}</h1>", unsafe_allow_html=True)
    st.markdown("""<div>&nbsp;</div> """,unsafe_allow_html=True)
    sharks_presence_count=count_shark_presence(season_df,season_sharks)
    sharks_deal_count=count_shark_deal(season_df,season_sharks)
    
    if st.session_state.selected_season == 0:
        pass
    else:
        # Creating a layout with columns
        col1, col2, col3, col4 = st.columns(4) 
        with col1:
            metric_card("Show Host", season_df['Anchor'].mode()[0],"             ")
        with col2:
            metric_card("Season start Date", season_df['Season Start'].min(),"         ")
        with col3:
            metric_card("Season Last date", season_df['Season End'].max(),"          ")
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
        metric_card("Highest Equity Given ( in ₹ )", f"₹{season_df['Total Deal Equity'].max()} %",season_df.loc[season_df['Total Deal Equity'] == season_df['Total Deal Equity'].max(), 'Startup Name'].values[0])
    with col11: 
        metric_card("Highest Pitches witnessed", 
            f" {sharks_presence_count[max(sharks_presence_count, key=sharks_presence_count.get)]}", 
            max(sharks_presence_count, key=sharks_presence_count.get))
    with col12:
        metric_card("Highest deals done", 
            f"{sharks_deal_count[max(sharks_deal_count, key=sharks_deal_count.get)]}", 
            max(sharks_deal_count, key=sharks_deal_count.get))
    
    st.markdown("----")
    col20, col22 = st.columns(2)
    with col20:
        st.markdown("<h1 style='text-align: center;'>Total Investment by Sharks</h1>", unsafe_allow_html=True)
        color_scale = [(0, 'rgb(204, 231, 255)'),  # Lightest blue at 0
               (1, 'rgb(0, 51, 102)')]   # Darkest blue at 1
        dictt=count_shark_deal_amount(season_df,season_sharks) 
        df = pd.DataFrame(list(dictt.items()), columns=['sharks', 'Amount in Cr'])
        fig = px.bar(df, x='sharks', y='Amount in Cr', 
             color='Amount in Cr',color_continuous_scale=color_scale)

        # Show the plot
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
 
    col30,col31 = st.columns(2)
    with col30:
        pass
    
#sharks data function part2 of the function
def sharks(season_df,guests_list):
    st.markdown("""<h1  style='text-align: center;font-family: \"Times New Roman\", serif; color: #FFD700;'>Shark Analysis</h1>""", unsafe_allow_html=True)
    col100,col101,col102,col103,col104,col105,col106,col107=st.columns([1,2,2,2,2,2,2,1])
    with col101:
        st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
        Namita = st.button("Namita", key="S1")
        st.markdown("</div>", unsafe_allow_html=True)
    with col102:
        st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
        Vineeta = st.button("Vineeta", key="S2")
        st.markdown("</div>", unsafe_allow_html=True)
    with col103:
        st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
        Anupam = st.button("Anupam", key="S3")
        st.markdown("</div>", unsafe_allow_html=True)
    with col104:
        st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
        Aman = st.button("Aman", key="S4")
    st.markdown("</div>", unsafe_allow_html=True)
    with col105:
        st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
        Peyush = st.button("Peyush", key="S5")
        st.markdown("</div>", unsafe_allow_html=True)
    with col106:
        st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
        Guests = st.button("Guests", key="S6")
        st.markdown("</div>", unsafe_allow_html=True)
        
        
    if Namita:
        st.session_state.selected_shark = "Namita"
    elif Vineeta:
        st.session_state.selected_shark = "Vineeta"
    elif Anupam:
       st.session_state.selected_shark = "Anupam"
    elif Aman:
        st.session_state.selected_shark = "Aman"
    elif Peyush:
        st.session_state.selected_shark = "Peyush"
    elif Guests:
        st.session_state.selected_shark = "Guests"
        
    
    
    
    if st.session_state.selected_shark == "Namita":
        sharks_info(season_df,"Namita","Namita", "CEO, Emcure Pharmaceuticals", "MBA, Wharton School of the University of Pennsylvania",guests_list)
    elif st.session_state.selected_shark == "Vineeta":
        sharks_info(season_df,"Vineeta","Vineeta Singh", "CEO, SUGAR Cosmetics", "IIM Ahmedabad",guests_list)
    elif st.session_state.selected_shark == "Anupam":
        sharks_info(season_df,"Anupam","Anupam Mittal", "Founder & CEO, Shaadi.com", "MBA, Boston College",guests_list)
    elif st.session_state.selected_shark == "Aman":
        sharks_info(season_df,"Aman","Aman Gupta", "Co-Founder and CMO, boAt", "MBA, ISB Hyderabad",guests_list)
    elif st.session_state.selected_shark == "Peyush":
        sharks_info(season_df,"Peyush","Peyush Bansal", "Founder & CEO, Lenskart", "IIM Bangalore",guests_list)
    elif st.session_state.selected_shark == "Guests":
        sharks_info(season_df,"NA","NA","NA","NA",guests_list)
        
   
#pitches details function part 3
def pitches_metrics(ses_df,season_sharks ):
    st.markdown("""<h1  style='text-align: center;font-family: \"Times New Roman\", serif; color: #FFD700;'>Pitch(Company) Details</h1>""", unsafe_allow_html=True)
    startup_names = ses_df["Startup Name"].dropna().unique().tolist()
    col31, col32, col33,col34, col35=st.columns([1,1,1,1,1])
    with col33:
        selected_startup = st.selectbox("Select a Startup", options=startup_names, index=None, placeholder="Search and select")
    if not selected_startup and startup_names:  # Check if no startup is selected AND there are startups available
        selected_startup = startup_names[0]   
    if selected_startup:
        selected_startup_data = ses_df[ses_df["Startup Name"] == selected_startup].iloc[0]
        st.markdown(f"<h2 style='text-align: center; color: #FFD700;'>{selected_startup} Details</h2>", unsafe_allow_html=True)
        st.markdown(f"<h5 style='text-align: center;font-size: 18px'>{selected_startup_data['Business Description']}</h5>", unsafe_allow_html=True) 
        st.subheader("Pitch Overview")
        #section1
        col1, col2, col3 = st.columns(3)
        with col1:
            metric_card("Received Offer", "Yes" if selected_startup_data["Received Offer"] == 1 else "No")
        with col2:
            metric_card("Startup Industry", selected_startup_data["Industry"])
        with col3:
            metric_card("Number of Presenters", str(selected_startup_data["Number of Presenters"]))

        #section2
        col4, col5, col6 = st.columns(3)
        with col4:
            metric_card("Original Air Date", selected_startup_data["Original Air Date"])
        with col5:
            metric_card("Pitchers State", selected_startup_data["Pitchers State"])
        with col6:
            metric_card("Average Pitcher Age", selected_startup_data["Pitchers Average Age"])
            
        # Section 3
        st.subheader("Initial Funding Details")
        col7, col8, col9 = st.columns(3)
        with col7:
            metric_card("Original Ask Amount", f"₹{selected_startup_data['Original Ask Amount']/ 100:.2f} Cr")
        with col8:
            metric_card("Original Offered Equity", f"{selected_startup_data['Original Offered Equity']}%")
        with col9:
             metric_card("Valuation Requested", f"₹{selected_startup_data['Valuation Requested']/100:.2f}Cr")
             
        if selected_startup_data["Received Offer"] == 0:
            st.write(" ")
            st.write(f"<h2 style='text-align: center; color: #FFD700;'>This pitch has not received the offer</h2>", unsafe_allow_html=True)
            st.write(" ")
        elif selected_startup_data["Accepted Offer"] == 0 and selected_startup_data["Received Offer"] == 1:
            st.write(" ")
            st.write(f"<h2 style='text-align: center; color: #FFD700;'>This pitch has received the offer but not accepted</h2>", unsafe_allow_html=True)
            st.write(" ")
        else:
            st.subheader("Final Funding Details")
            col10, col11, col12 = st.columns(3)
            with col10:
                metric_card("Total Deal Amount", f"₹{selected_startup_data['Total Deal Amount']/100:.2f}Cr")
            with col11:
                metric_card("Total Deal Equity", f"{selected_startup_data['Total Deal Equity']:.2f}%")
            with col12:
                metric_card("Deal Valuation", f"₹{selected_startup_data['Deal Valuation']/100:.2f}Cr")
            #sectio 5
            col13, col14, col15 = st.columns(3) 
            with col13:
                metric_card("No. of Sharks in Deal", str(selected_startup_data["Number of Sharks in Deal"]))
            with col14:
                sharks_in_deal = []
                for shark in season_sharks:
                    if selected_startup_data.get(f"{shark} Deal", 0) == 1:
                         sharks_in_deal.append(shark)
                metric_card("Sharks in Deal", ", ".join(sharks_in_deal) if sharks_in_deal else "None")
        
 
# Custom CSS for Gradient Background
st.markdown("""
    <style>
    /* Full page gradient background */
    body, .stApp {
        background: #292b32 !important;
        font-family: Arial;
        color: white !important;
    }

    /* Centered bold uppercase yellow title */
    .title {
        text-align: center;
        font-weight: 900;
        font-size: 10em;
        color: #FFD700; /* Gold Yellow */
        text-transform: uppercase;
    }

    /* Button styling */
    .stButton>button {
        width: 150px;
        font-weight: bold;
        font-size: 32px;
        padding: 18px;
        border-radius: 8px;
        border: 4px solid #0a91bd !important; /* Blue Border */
        cursor: pointer;
        text-align: center;
        background-color: transparent !important;
        color: white !important;
    }

    /* Hover effect */
    .stButton>button:hover {
        background-color: rgba(10, 145, 189, 0.2) !important; /* Light Blue on Hover */
    }

     
    </style>
""", unsafe_allow_html=True)

#-------------------------------------------------------------------------------
# Creating logo and images
st.image("logo_image.png")   
st.markdown("---")

# Season selection buttons
col1, col2, col3 = st.columns([1, 4, 1])
with col2:
    sub_col1, sub_col2, sub_col3, sub_col4, sub_col5, sub_col6, sub_col7,sub_col8,sub_col9 = st.columns(
        [1, 10, 2, 10, 2, 10, 2, 10, 1]
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
    with sub_col8:
        st.markdown("<div style='display: flex; justify-content: center;'>", unsafe_allow_html=True)
        overall = st.button("Overall", key="ov")
        st.markdown("</div>", unsafe_allow_html=True)
            



 
# Handling button clicks (using session state)
if season1:
    st.session_state.selected_season = 1
elif season2:
    st.session_state.selected_season = 2
elif season3:
    st.session_state.selected_season = 3
elif overall:
    st.session_state.selected_season = 0


# Displaying the correct season (using session state)
if st.session_state.selected_season == 1:
    argument = "  📊 Season 1 Analysis!"
    season_sharks=season1_sharks+season1_guests
    seasons_data(argument, season1_df,season_sharks)
    st.markdown("---")
    sharks(season1_df,season1_guests) 
    st.markdown("---")
    pitches_metrics(season1_df,season1_sharks) 
   
elif st.session_state.selected_season == 2:
    argument = "  📊 Season 2 Analysis!" 
    season_sharks=season2_sharks+season2_guests
    seasons_data(argument, season2_df,season_sharks)
    st.markdown("---")
    sharks(season2_df,season2_guests)
    st.markdown("---")
    pitches_metrics(season2_df,season2_sharks)   
  
elif st.session_state.selected_season == 3:
    argument = "  📊 Season 3 Analysis!" 
    season_sharks=season3_sharks+season3_guests
    seasons_data(argument, season3_df,season_sharks)
    st.markdown("---")
    sharks(season3_df,season3_guests)
    st.markdown("---")
    pitches_metrics(season3_df,season3_sharks)

elif st.session_state.selected_season == 0:
    argument = " Overall Seasons Analysis!" 
    season_sharks=season3_sharks+season3_guests
    seasons_data(argument, filtered_df,All_sharks)
    st.markdown("---")
    sharks(filtered_df,All_guests)
    st.markdown("---")
    pitches_metrics(filtered_df,All_guests)
    
else:
    argument = "  📊 Season 1 Analysis!" 
    season_sharks=season1_sharks+season1_guests
    seasons_data(argument, season1_df,season1_sharks)
    st.markdown("---")
    sharks(season1_df,season1_guests)
    st.markdown("---")
    pitches_metrics(season1_df,season1_sharks)
      

st.title("📊 Number of Presenters vs. Pitches & Accepted Offers")
df=pd.read_csv("filtered_df.csv")
# Aggregating data: Count of pitches and accepted offers per number of presenters
presenter_counts = df.groupby("Number of Presenters").agg(
    Total_Pitches=("Number of Presenters", "count"),
    Accepted_Offers=("Accepted Offer", "sum")
).reset_index()

# Creating a grouped bar chart using Plotly Express
fig = px.bar(
    presenter_counts,
    x="Number of Presenters",
    y=["Total_Pitches", "Accepted_Offers"],
    barmode="group",  # Side-by-side bars
    color_discrete_map={
        "Total_Pitches": "rgb(204, 231, 255)",  # Lightest blue
        "Accepted_Offers": "rgb(0, 51, 102)"  # Dark blue
    },
    labels={"value": "Count", "variable": "Category"},
    title="Number of Presenters vs. Pitches & Accepted Offers"
)

# Update layout for better readability
fig.update_layout(
    xaxis_title="Number of Presenters",
    yaxis_title="Count",
    legend_title="Category",
    bargap=0.2
)

# Display the chart
st.plotly_chart(fig, use_container_width=True)

# Insight
max_presenters = presenter_counts.loc[presenter_counts["Accepted_Offers"].idxmax(), "Number of Presenters"]
st.write(f"💡 **Insight:** Startups with **{max_presenters} presenters** received the most offers! Maybe it's time to launch your business with friends! 🚀")
 
 
 
st.title("🦈 Shark Participation in Deals")

# Aggregating shark participation in deals
shark_deals = df[["Aman Deal", "Namita Deal", "Peyush Deal", "Vineeta Deal", "Anupam Deal", "Ashneer Deal"]].sum()
shark_deals_df = pd.DataFrame({"Shark": shark_deals.index, "Deals": shark_deals.values})

# Creating the pie chart (Display Shark names & percentages)
fig_shark = px.pie(
    shark_deals_df,
    names="Shark",
    values="Deals",
    title="Which Shark Invested the Most?",
    color_discrete_sequence=px.colors.sequential.Blues
)

# Update layout to show names & percentages, and hide legend
fig_shark.update_traces(textinfo="label+percent")  # Show Shark names & percentages
fig_shark.update_layout(showlegend=False)  # Hide side legend markers

# Show figure
st.plotly_chart(fig_shark, use_container_width=True)


st.markdown("---")

st.markdown("""
    <div style="background-color: black; padding: 20px; border-radius: 10px;">
        <h2 style='text-align: center; color: #FFD700;'>About This Dashboard</h2>
        <p style='text-align: center; font-size: 16px; color: #bbb;'>
            This dashboard provides an interactive analysis of <strong>Shark Tank India</strong> data. 
            It allows users to explore season-wise statistics, shark-specific metrics, and detailed insights 
            into individual pitches. The goal is to make the data accessible and engaging for fans, 
            entrepreneurs, and data enthusiasts alike.
        </p>
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div style="background-color: black; padding: 20px; border-radius: 10px;">
        <h2 style='text-align: center; color: #FFD700;'>What is Shark Tank?</h2>
        <p style='text-align: center; font-size: 16px; color: #bbb;'>
            <strong>Shark Tank</strong> is a popular reality TV show where entrepreneurs pitch their business ideas 
            to a panel of investors (called "sharks") in hopes of securing funding. In exchange, the sharks 
            receive equity in the business. The show is known for its intense negotiations, innovative ideas, 
            and inspiring success stories. <strong>Shark Tank India</strong> brings this concept to the Indian audience, 
            featuring some of the country's most prominent business leaders as sharks.
        </p>
    </div>
""", unsafe_allow_html=True)

# Key Terms Explanation (Expandable Section)
with st.expander("**Key Terms Explained**", expanded=False):
    st.markdown("""
        <div style="background-color: black; padding: 20px; border-radius: 10px;">
            <p style="color: #fff; font-size: 16px;">
                <strong>1. Sharks:</strong> The investors on the show who provide funding to entrepreneurs in exchange for equity in their business.<br>
                <strong>2. Equity:</strong> The percentage of ownership in a company that is given to the sharks in exchange for their investment.<br>
                <strong>3. Deal Valuation:</strong> The total value of the company as agreed upon during the deal negotiation.<br>
                <strong>4. Pitch:</strong> The presentation made by entrepreneurs to convince the sharks to invest in their business.<br>
                <strong>5. Original Ask Amount:</strong> The amount of money the entrepreneur initially requests from the sharks.<br>
                <strong>6. Total Deal Amount:</strong> The final amount of money invested by the sharks in the business.<br>
                <strong>7. Received Offer:</strong> Indicates whether the entrepreneur received an investment offer from any shark.<br>
                <strong>8. Accepted Offer:</strong> Indicates whether the entrepreneur accepted the investment offer from the sharks.<br>
            </p>
        </div>
    """, unsafe_allow_html=True)

# Personal Info Section (NO CHANGES HERE)
st.markdown(
    """
    ### ✨ Nissi Grace Chinamuttevi  
    **👩‍💻 Developer & Data Enthusiast**   

    ### 📬 Get in Touch  
    📧 **Email:** [nissigracech@gmail.com](mailto:nissigracech@gmail.com)  
    🔗 **GitHub:** [Project Repository](https://github.com/nissigracech)  
    🌐 **LinkedIn profile:** [Nissi Grace](https://www.linkedin.com/in/nissi-grace-chinamuttevi-47b693224/) 
    """, 
    unsafe_allow_html=True
)


 
# CSS for Sticky Bottom-Right Box
st.markdown("""
    <style>
    .sticky-bottom-right {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background-color: #161616;
        padding: 10px;
        padding-bottom: 20px;
        border-radius: 10px;
        box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1);
        z-index: 1000;
        border: 2px solid #FFD700;
    }
    </style>
""", unsafe_allow_html=True)

# Small Box in Bottom-Right Corner
st.markdown("""
    <div class="sticky-bottom-right">
        <p style='text-align: center; font-size: 12px; color: #bbb; margin: 0;'>Created by</p>
        <h4 style='color: #FFD700; text-align: center; font-size: 16px; font-weight: bold; margin: 0; line-height: 1.4;'>
            Nissi Grace Chinamuttevi
        </h4>
    </div>
    """, unsafe_allow_html=True)
