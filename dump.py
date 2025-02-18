import streamlit as st
import plotly.express as px
import pandas as pd

# Sample data
data = pd.DataFrame({
    'Category': ['A', 'B', 'C', 'D', 'E'],
    'Value': [100, 200, 150, 250, 180],
    'Details': [
        "🔹 **Category A:** This represents the first category with insights.",
        "🔹 **Category B:** This has the highest value among all categories.",
        "🔹 **Category C:** This is an average category in the dataset.",
        "🔹 **Category D:** This is the second-highest category.",
        "🔹 **Category E:** This is a moderate category with steady growth."
    ]
})

# Create a bar chart using Plotly
fig = px.bar(data, x='Category', y='Value', text='Value')

# Enable click interaction
selected_category = st.session_state.get("selected_category", None)

def on_click(trace, points, state):
    if points.points:
        selected_category = points.points[0]['x']
        st.session_state["selected_category"] = selected_category

fig.update_traces(marker_color='blue', textposition='outside')
fig.data[0].on_click(on_click)

# Display the chart
st.plotly_chart(fig)

# Show styled details when a bar is clicked
if selected_category:
    details = data[data['Category'] == selected_category]['Details'].values[0]
    
    # Styling with Markdown
    st.markdown(f"""
        <div style="
            background-color: #f4f4f4; 
            padding: 15px; 
            border-radius: 10px; 
            box-shadow: 2px 2px 5px rgba(0,0,0,0.1);
            font-size: 16px;">
            <b style="color: #333;">Details for {selected_category}:</b> <br>
            {details}
        </div>
    """, unsafe_allow_html=True)
