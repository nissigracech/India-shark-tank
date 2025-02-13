import streamlit as st
import pandas as pd
import plotly.express as px

# Load Data
def load_data():
    file_path = "Shark Tank India Dataset.csv"  # Update path if needed
    df = pd.read_csv(file_path)
    df = df.drop(columns=[col for col in df.columns if "Unnamed" in col])  # Remove unnecessary columns
    return df

df = load_data()

# Streamlit Page Config
st.set_page_config(page_title="Shark Tank India Dashboard", layout="wide")


season = st.sidebar.selectbox('Select season', ['Season 2', 'Season 1'])


# Custom Sidebar Styling
st.markdown(
    """
    <style>
        [data-testid="stSidebar"] {
            background-color: #0A1931;
        }
        [data-testid="stAppViewContainer"] {
            background-color: #F0F2F6;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Dashboard Title
st.title("📊 Shark Tank India Analytics Dashboard")

# Metrics Section
col1, col2, col3 = st.columns(3)
col1.metric("Total Pitches", len(df))
col2.metric("Total Deals", df['deal'].sum())
col3.metric("Success Rate", f"{(df['deal'].sum() / len(df) * 100):.2f}%")

# Funding Amount Distribution
st.subheader("💰 Investment Distribution")
deal_distribution = df[['deal_amount']].dropna()
fig = px.histogram(deal_distribution, x='deal_amount', nbins=20, title="Distribution of Deal Amounts", color_discrete_sequence=['#FF5733'])
st.plotly_chart(fig, use_container_width=True)

# Top Investors
st.subheader("🦈 Top Investing Sharks")
sharks = ['ashneer_deal', 'anupam_deal', 'aman_deal', 'namita_deal', 'vineeta_deal', 'peyush_deal', 'ghazal_deal']
investor_deals = df[sharks].sum().sort_values(ascending=False)
fig2 = px.bar(investor_deals, x=investor_deals.index, y=investor_deals.values, title="Sharks with Most Investments", color_discrete_sequence=['#1E90FF'])
st.plotly_chart(fig2, use_container_width=True)
