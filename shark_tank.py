import streamlit as st

# Set page config
st.set_page_config(page_title="Shark Tank India EDA Dashboard", layout="wide")

# Centered bold title
st.markdown("""
    <style>
        .title {
            text-align: center;
            font-weight: bold;
            font-size: 2em;
        }
    </style>
    <h1 class="title">Shark Tank India EDA Dashboard</h1>
""", unsafe_allow_html=True)


# Create three buttons below the title
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Overview"):
        st.write("You clicked Overview!")

with col2:
    if st.button("Investment Analysis"):
        st.write("You clicked Investment Analysis!")

with col3:
    if st.button("Startup Insights"):
        st.write("You clicked Startup Insights!")
