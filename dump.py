import streamlit as st
import pandas as pd
import plotly.express as px

# Sample data with Indian states and values
data = pd.DataFrame({
    "state": ["Maharashtra", "Karnataka", "Delhi", "Tamil Nadu", "Gujarat"],
    "value": [100, 80, 90, 70, 60]  # Example values (could be startup count, funding, etc.)
})

# Load India GeoJSON (for state boundaries)
INDIA_GEOJSON = "https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json"

# Create a choropleth map
fig = px.choropleth(
    data,
    geojson="https://raw.githubusercontent.com/vega/datalib/master/data/india-states.json",  # GeoJSON for India
    locations="state",
    featureidkey="properties.st_nm",  # Match state names from GeoJSON
    color="value",
    color_continuous_scale="Blues",
    title="State-wise Data in India"
)

fig.update_geos(fitbounds="locations", visible=False)  # Adjust map zoom

# Streamlit app
st.title("India State-wise Map in Streamlit")
st.plotly_chart(fig)
