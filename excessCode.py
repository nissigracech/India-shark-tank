#code for only shark tank image

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
