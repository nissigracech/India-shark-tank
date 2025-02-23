#code for only shark tank image
'''
# Create three main columns (col2 is the center column)
col1, col2, col3 = st.columns([1, 5, 1])  

with col2:  # Center the content
    sub_col1, sub_col2, sub_col3 = st.columns([1, 1, 1])  # Nested columns inside col2

    with sub_col2:  # Image inside the middle sub-column
        st.image("stilogo.png", caption="Shark Tank India S1", width=300)
        
        
with col1:
    with st.container():
        st.write("Column 1")
        st.markdown("<div style='height: 100px; background-color: red;'></div>", unsafe_allow_html=True)

with col2:
    with st.container():
        st.write("Column 2")
        st.markdown("<div style='height: 100px; background-color: blue;'></div>", unsafe_allow_html=True)

with col3:
    with st.container():
        st.write("Column 3")
        st.markdown("<div style='height: 100px; background-color: green;'></div>", unsafe_allow_html=True)
'''

from PIL import Image, ImageDraw, ImageFont

# Load the background image
background = Image.open("bc.jpg")

# Create a new image with the same size as the background
img = background.copy()
draw = ImageDraw.Draw(img)

# Add text (optional)
text = "Shark Tank India Dashboard"
font = ImageFont.load_default()  # You can use a custom font
text_position = (50, 50)  # Adjust as needed
text_color = (255, 255, 255)  # White color
draw.text(text_position, text, fill=text_color, font=font)

# Save the new image
img.save("final_image.png")
print("Image saved successfully!")















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














st.markdown("""
    <style>
        /* Center the select box */
        div[data-testid="stSelectbox"] {
            width: 100% !important;
        }

        /* Apply the gradient background */
        div[data-baseweb="select"] > div {
            background: linear-gradient(135deg, #050A13, #0B132B, #1B263B, #415A77) !important;
            color: white !important;
            border-radius: 8px;
            padding: 8px;
            border: 1px solid rgba(255, 255, 255, 0.3);
        }

        /* Ensure selected text is visible */
        div[data-testid="stSelectbox"] span {
            color: white !important;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)






col1, col2, col3 = st.columns([4,1, 15])  
with col1:
    st.image("stilogo.png", caption=" ", width=400)  # Smaller Image

with col3:
    st.image("st.png", caption=" ", width=1000)  # Larger Image



data = {
    'Category': ['A', 'B', 'C', 'D'],
    'Value1': [10, 20, 30, 40],
    'Value2': [15, 25, 35, 45],
    'Value3': [5, 10, 15, 20]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Set up the Streamlit app
st.title("Stacked Bar Chart Example with Plotly")

# Display the DataFrame
st.write("Data:")
st.dataframe(df)

# Create a stacked bar chart with Plotly
fig = px.bar(df, x='Category', y=['Value1', 'Value2', 'Value3'], title='Stacked Bar Chart', barmode='stack')
st.plotly_chart(fig)






st.markdown(f"<h1 style='text-align: center;'>sharks analysis</h1>", unsafe_allow_html=True)
col100,col101,col102,col103,col104,col105,col106=st.columns([1,2,2,2,2,2,1])
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
    
    
    
    
if st.session_state.selected_shark == "Namita":
        shark_info_card("Namita", "CEO, Emcure Pharmaceuticals", "MBA, Wharton School of the University of Pennsylvania", "Namita.jpg")
        
    elif st.session_state.selected_shark == "Vineeta":
        shark_info_card("Vineeta Singh", "CEO, SUGAR Cosmetics", "IIM Ahmedabad", "Vineeta.jpg")
    elif st.session_state.selected_shark == "Anupam":
        shark_info_card("Anupam Mittal", "Founder & CEO, Shaadi.com", "MBA, Boston College", "Anupam.jpg")
    elif st.session_state.selected_shark == "Aman":
        shark_info_card("Aman Gupta", "Co-Founder and CMO, boAt", "MBA, ISB Hyderabad", "Aman.jpg")
    elif st.session_state.selected_shark == "Peyush":
        shark_info_card("Peyush Bansal", "Founder & CEO, Lenskart", "IIM Bangalore", "Peyush.jpg")
        
        
      st.markdown(f"""
    <div style="border: 1px solid #ccc; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
        <div style="display: flex; align-items: center;">  
            <div style="width: 150px; margin-right: 20px;">  
                <img src="{image_filename}" style="width: 100%; border-radius: 5px;">
            </div>
            <div>
                <h3 style="margin-top: 0;">{shark_name}</h3>
                <p><strong>Occupation:</strong> {occupation}</p>
                <p><strong>Education:</strong> {education}</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)      
        
if st.session_state.selected_shark == "Namita":
        shark_info_card("Namita", "CEO, Emcure Pharmaceuticals", "MBA, Wharton School of the University of Pennsylvania", "Namita.jpg")
        
    elif st.session_state.selected_shark == "Vineeta":
        shark_info_card("Vineeta Singh", "CEO, SUGAR Cosmetics", "IIM Ahmedabad", "Vineeta.jpg")
    elif st.session_state.selected_shark == "Anupam":
        shark_info_card("Anupam Mittal", "Founder & CEO, Shaadi.com", "MBA, Boston College", "Anupam.jpg")
    elif st.session_state.selected_shark == "Aman":
        shark_info_card("Aman Gupta", "Co-Founder and CMO, boAt", "MBA, ISB Hyderabad", "Aman.jpg")
    elif st.session_state.selected_shark == "Peyush":
        shark_info_card("Peyush Bansal", "Founder & CEO, Lenskart", "IIM Bangalore", "Peyush.jpg")
        
        
        plt.figure(figsize=(10, 6))
    plt.plot(key_deals['Startup Name'], key_deals['deal_amount_per_shark'], marker='o', label='Column b')
    plt.plot(key_deals['Startup Name'], key_deals['equity_per_shark'], marker='o', label='Column c')
    plt.plot(key_deals['Startup Name'], key_deals['Original Ask Amount'], marker='*', label='Column d')

    plt.xlabel('Column a (Categories)')
    plt.ylabel('Values')
    plt.title('Multiline Chart of b, c, and d vs. a')
    plt.legend()
    plt.grid(True)  # Add a grid for better readability (optional)
    plt.xticks(rotation=90, ha='right')  # Rotate x-axis labels if they are long
    plt.tight_layout() # Adjust layout to prevent labels from overlapping
    st.write("Hi")
    plt.show()
    
    col31,col32=st.columns(2)
    with col31:
        deals_labels = list(sharks_deal_count.keys())
        deals_values = list(sharks_deal_count.values())
        fig = px.bar(x=deals_labels, y=deals_values, title="hi", labels={"x": "Labels", "y": "Values"}) # Correct px usage

        st.plotly_chart(fig)
    with col32:
        deals_labels = list(sharks_presence_count.keys())
        deals_values = list(sharks_presence_count.values())
        fig = px.bar(x=deals_labels, y=deals_values, title="hi", labels={"x": "Labels", "y": "Values"}) # Correct px usage

        st.plotly_chart(fig)
        
        
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from PIL import Image

# Set page config
st.set_page_config(page_title="Shark Tank India", layout="wide")

# Load the pre-processed data
filtered_df = pd.read_csv("filtered_df.csv")

# categorise the data for each season
season1_df=filtered_df[filtered_df['Season Number'] == 1]
season1_df.drop(columns=['Ritesh Present',  'Ritesh Deal', 
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
        color: #FFD700; /* Gold color */
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
    
def sharks_info(season_df,key,shark_name, occupation, education):
    image_info=key+".jpg"
    col400,col401,col402,col403=st.columns([3,4,7,3])
    with col401:
        st.image(image_info,width=300)
    with col402:
        shark_info_metric_card(shark_name,occupation,education)
        pass
    
    # begin of shark metric cards
    #section 1
    deal=key+" Deal"
    present=key+" Present"
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
    st.markdown(f"<h1 style='text-align: center;'>{argument}</h1>", unsafe_allow_html=True)
    sharks_presence_count=count_shark_presence(season_df,season_sharks)
    sharks_deal_count=count_shark_deal(season_df,season_sharks)
    
    
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
        state_counts = season_df["Pitchers State"].value_counts()

        # Create pie chart
        fig, ax = plt.subplots()
        ax.pie(state_counts, labels=state_counts.index, autopct="%1.1f%%", startangle=140)
        ax.set_title("Distribution of Pitchers by State")

        # Show the plot
        st.pyplot(fig)
    
        

#sharks data function part2 of the function
def sharks(season_df):
    col100,col101,col102,col103,col104,col105,col106=st.columns([1,2,2,2,2,2,1])
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
    
    
    
    if st.session_state.selected_shark == "Namita":
        sharks_info(season_df,"Namita","Namita", "CEO, Emcure Pharmaceuticals", "MBA, Wharton School of the University of Pennsylvania")
    elif st.session_state.selected_shark == "Vineeta":
        sharks_info(season_df,"Vineeta","Vineeta Singh", "CEO, SUGAR Cosmetics", "IIM Ahmedabad")
    elif st.session_state.selected_shark == "Anupam":
        sharks_info(season_df,"Anupam","Anupam Mittal", "Founder & CEO, Shaadi.com", "MBA, Boston College")
    elif st.session_state.selected_shark == "Aman":
        sharks_info(season_df,"Aman","Aman Gupta", "Co-Founder and CMO, boAt", "MBA, ISB Hyderabad")
    elif st.session_state.selected_shark == "Peyush":
        sharks_info(season_df,"Peyush","Peyush Bansal", "Founder & CEO, Lenskart", "IIM Bangalore")
   
#pitches details function part 3
def pitches_metrics(ses_df,season_sharks ):
    startup_names = ses_df["Startup Name"].dropna().unique().tolist()
    col31, col32, col33,col34, col35=st.columns([1,1,1,1,1])
    with col33:
        selected_startup = st.selectbox("Select a Startup", options=startup_names, index=None, placeholder="Search and select")
    if not selected_startup and startup_names:  # Check if no startup is selected AND there are startups available
        selected_startup = startup_names[0]   
    if selected_startup:
        selected_startup_data = ses_df[ses_df["Startup Name"] == selected_startup].iloc[0]
        st.markdown(f"<h2 style='text-align: center; color: #FFD700;'>{selected_startup} Details</h2>", unsafe_allow_html=True)
        st.markdown(f"<h5 style='text-align: center;font-size: 18px'>{selected_startup} Details</h5>", unsafe_allow_html=True) 
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



 
# Handling button clicks (using session state)
if season1:
    st.session_state.selected_season = 1
elif season2:
    st.session_state.selected_season = 2
elif season3:
    st.session_state.selected_season = 3

#st.image("Namita.png")

# Displaying the correct season (using session state)
if st.session_state.selected_season == 1:
    argument = "  📊 Season 1 Analysis!"
    season_sharks=season1_sharks+season1_guests
    seasons_data(argument, season1_df,season_sharks)
    st.markdown("---")
    sharks(season1_df) 
    st.markdown("---")
    pitches_metrics(season1_df,season1_sharks)    
elif st.session_state.selected_season == 2:
    argument = "  📊 Season 2 Analysis!" 
    season_sharks=season2_sharks+season2_guests
    seasons_data(argument, season2_df,season_sharks)
    st.markdown("---")
    sharks(season2_df)
    st.markdown("---")
    pitches_metrics(season2_df,season2_sharks)     
elif st.session_state.selected_season == 3:
    argument = "  📊 Season 3 Analysis!" 
    season_sharks=season3_sharks+season3_guests
    seasons_data(argument, season3_df,season_sharks)
    st.markdown("---")
    sharks(season3_df)
    st.markdown("---")
    pitches_metrics(season1_df,season3_sharks)
else:
    argument = "  📊 Season 1 Analysis!" 
    season_sharks=season1_sharks+season1_guests
    seasons_data(argument, season1_df,season1_sharks)
    st.markdown("---")
    sharks(season1_df)
    st.markdown("---")
    pitches_metrics(season1_df,season1_sharks)
      

 
st.markdown("---")

# Section for Basic Info
st.markdown("""
    <h2 style='text-align: center; color: #FFD700;'>About This Dashboard</h2>
    <p style='text-align: center; font-size: 16px; color: #bbb;'>
        This dashboard provides an interactive analysis of <strong>Shark Tank India</strong> data. 
        It allows users to explore season-wise statistics, shark-specific metrics, and detailed insights 
        into individual pitches. The goal is to make the data accessible and engaging for fans, 
        entrepreneurs, and data enthusiasts alike.
    </p>
""", unsafe_allow_html=True)

# Section for What Shark Tank Is
st.markdown("""
    <h2 style='text-align: center; color: #FFD700;'>What is Shark Tank?</h2>
    <p style='text-align: center; font-size: 16px; color: #bbb;'>
        <strong>Shark Tank</strong> is a popular reality TV show where entrepreneurs pitch their business ideas 
        to a panel of investors (called "sharks") in hopes of securing funding. In exchange, the sharks 
        receive equity in the business. The show is known for its intense negotiations, innovative ideas, 
        and inspiring success stories. <strong>Shark Tank India</strong> brings this concept to the Indian audience, 
        featuring some of the country's most prominent business leaders as sharks.
    </p>
""", unsafe_allow_html=True)
st.markdown("""
<div style="background-color: #161616; padding: 20px; border-radius: 10px; margin-bottom: 20px;">
    <h3 style="color: #FFD700; font-weight: bold;">Dashboard Created By</h3>
    <p style="color: #eee; line-height: 1.6;">
        [Your Name/Team Name]
    </p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
    <div style='text-align: center; margin-top: 30px; font-size: 14px; color: #888;'>
        <p>Created with ❤️ using Streamlit</p>
        <p>Data Source: Shark Tank India</p>
    </div>
""", unsafe_allow_html=True)


# Add a horizontal line for separation
st.markdown("---")

# Gradient Background for the Info Section
st.markdown("""
    <style>
    .gradient-bg {
        background: #325f8c;
        padding: 20px;
        border-radius: 10px;
        color: white;
    }
    </style>
""", unsafe_allow_html=True)

# Section for Basic Info with Gradient Background
st.markdown("""
    <div class="gradient-bg">
        <h2 style='text-align: center; color: #FFD700;'>About This Dashboard</h2>
        <p style='text-align: center; font-size: 16px; color: #fff;'>
            This dashboard provides an interactive analysis of <strong>Shark Tank India</strong> data. 
            It allows users to explore season-wise statistics, shark-specific metrics, and detailed insights 
            into individual pitches. The goal is to make the data accessible and engaging for fans, 
            entrepreneurs, and data enthusiasts alike.
        </p>
    </div>
""", unsafe_allow_html=True)

# Section for What Shark Tank Is with Gradient Background
st.markdown("""
    <div class="gradient-bg">
        <h2 style='text-align: center; color: #FFD700;'>What is Shark Tank?</h2>
        <p style='text-align: center; font-size: 16px; color: #fff;'>
            <strong>Shark Tank</strong> is a popular reality TV show where entrepreneurs pitch their business ideas 
            to a panel of investors (called "sharks") in hopes of securing funding. In exchange, the sharks 
            receive equity in the business. The show is known for its intense negotiations, innovative ideas, 
            and inspiring success stories. <strong>Shark Tank India</strong> brings this concept to the Indian audience, 
            featuring some of the country's most prominent business leaders as sharks.
        </p>
    </div>
""", unsafe_allow_html=True)

# Footer (outside the gradient background)
st.markdown("""
    <div style='text-align: center; margin-top: 30px; font-size: 14px; color: #888;'>
        <p>Created with ❤️ using Streamlit</p>
        <p>Data Source: Shark Tank India</p>
    </div>
""", unsafe_allow_html=True)



# Add a horizontal line for separation
st.markdown("---")

# Gradient Background for the Info Section with Sticky Bottom
st.markdown("""
    <style>
    .gradient-bg {
        background: linear-gradient(to right, #000000, #000033, #000066, #000099, #0000cc, #0000ff);
        padding: 20px;
        border-radius: 10px;
        color: white;
    }
    .sticky-bottom {
        position: fixed;
        bottom: 0;
        left: 0;
        right: 0;
        z-index: 1000;
        background: linear-gradient(to right, #000000, #000033, #000066, #000099, #0000cc, #0000ff);
        padding: 20px;
        border-radius: 10px 10px 0 0;
        box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Section for Basic Info with Gradient Background and Sticky Bottom
st.markdown("""
    <div class="sticky-bottom">
        <h2 style='text-align: center; color: #FFD700;'>About This Dashboard</h2>
        <p style='text-align: center; font-size: 16px; color: #fff;'>
            This dashboard provides an interactive analysis of <strong>Shark Tank India</strong> data. 
            It allows users to explore season-wise statistics, shark-specific metrics, and detailed insights 
            into individual pitches. The goal is to make the data accessible and engaging for fans, 
            entrepreneurs, and data enthusiasts alike.
        </p>
        <h2 style='text-align: center; color: #FFD700;'>What is Shark Tank?</h2>
        <p style='text-align: center; font-size: 16px; color: #fff;'>
            <strong>Shark Tank</strong> is a popular reality TV show where entrepreneurs pitch their business ideas 
            to a panel of investors (called "sharks") in hopes of securing funding. In exchange, the sharks 
            receive equity in the business. The show is known for its intense negotiations, innovative ideas, 
            and inspiring success stories. <strong>Shark Tank India</strong> brings this concept to the Indian audience, 
            featuring some of the country's most prominent business leaders as sharks.
        </p>
        <div style='text-align: center; margin-top: 30px; font-size: 14px; color: #888;'>
            <p>Created with ❤️ using Streamlit</p>
            <p>Data Source: Shark Tank India</p>
        </div>
    </div>
""", unsafe_allow_html=True)




import streamlit as st

# Initialize session state
if "active_button" not in st.session_state:
    st.session_state.active_button = "Overall"

# Function to change active button
def set_active(button_name):
    st.session_state.active_button = button_name

# Define button styles using HTML & CSS
button_styles = """
    <style>
        .sidebar-button {
            display: block;
            width: 100%;
            padding: 12px;
            margin: 8px 0;
            text-align: center;
            border-radius: 8px;
            font-size: 16px;
            font-weight: bold;
            cursor: pointer;
            border: none;
            transition: all 0.3s;
        }
        .active {
            background-color: #ff4b4b; /* Red */
            color: white;
            box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.2);
        }
        .inactive {
            background-color: #f0f0f0;
            color: black;
        }
        .sidebar-button:hover {
            background-color: #ddd;
        }
    </style>
"""

st.markdown(button_styles, unsafe_allow_html=True)

# Sidebar buttons with custom styling
with st.sidebar:
    st.markdown("## 🎬 Select Season")

    buttons = ["Season 1", "Season 2", "Season 3", "Overall"]
    for button in buttons:
        btn_class = "active" if st.session_state.active_button == button else "inactive"
        
        if st.button(button, key=button):
            set_active(button)

# Display the selected option
st.write(f"### 📌 Currently Selected: {st.session_state.active_button}")

# Display different content based on selection
if st.session_state.active_button == "Season 1":
    st.write("📢 **Displaying data for Season 1...**")
elif st.session_state.active_button == "Season 2":
    st.write("📢 **Displaying data for Season 2...**")
elif st.session_state.active_button == "Season 3":
    st.write("📢 **Displaying data for Season 3...**")
else:
    st.write("📢 **Displaying overall data...**")
if "active_button" not in st.session_state:
    st.session_state.active_button = "Overall"

# Define button styles
def get_button_style(button_name):
    if st.session_state.active_button == button_name:
        return "background-color: #ff4b4b; color: white; font-weight: bold; border-radius: 10px; padding: 10px;"
    else:
        return "background-color: #f0f0f0; color: black; border-radius: 10px; padding: 10px;"

# Button click handler
def set_active(button_name):
    st.session_state.active_button = button_name

# Sidebar
with st.sidebar:
    st.markdown("### Select Season")

    if st.button("Season 1", on_click=set_active, args=("Season 1",)):
        pass
    if st.button("Season 2", on_click=set_active, args=("Season 2",)):
        pass
    if st.button("Season 3", on_click=set_active, args=("Season 3",)):
        pass
    if st.button("Overall", on_click=set_active, args=("Overall",)):
        pass

# Display the active selection
st.write(f"### Currently selected: {st.session_state.active_button}")