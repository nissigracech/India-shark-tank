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
    if st.button("Season 1"):
        st.write("season 1 analysis!")

with col2:
    if st.button("Season 2"):
        st.write("season 2 analysis Analysis!")

with col3:
    if st.button("Season 3"):
        st.write("season 3 analysis")
