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