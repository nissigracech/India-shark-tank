from PIL import Image, ImageDraw, ImageFont
import streamlit as st
import io

# Load the background image
background = Image.open("background.jpg")

# Create a copy to modify
img = background.copy()
draw = ImageDraw.Draw(img)

# Add text
text = "Shark Tank India Dashboard"
font = ImageFont.load_default()  # Default font (you can use a custom one)
text_position = (50, 50)  # Adjust position
text_color = (255, 255, 255)  # White text
draw.text(text_position, text, fill=text_color, font=font)

# Save image to a BytesIO object (instead of disk)
img_bytes = io.BytesIO()
img.save(img_bytes, format="PNG")
img_bytes.seek(0)  # Move to start of file

# Display image in Streamlit without saving it
st.image(img_bytes, use_column_width=True)