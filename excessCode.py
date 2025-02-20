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

