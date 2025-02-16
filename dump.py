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

# Custom Sidebar Styling


# Dashboard Title
st.title("📊 Shark Tank India Analytics Dashboard")

# Metrics Section
col1, col2, col3 = st.columns(3)
col1.metric("Total Pitches", len(df))
col2.metric("Total Deals", df['deal'].sum())
col3.metric("Success Rate", f"{(df['deal'].sum() / len(df) * 100):.2f}%")

# Buttons to Show Different Texts
if "message" not in st.session_state:
    st.session_state.message = "Click a button to see a change!"

col1, col2, col3 = st.columns(3)
if col1.button("Show Investment Insights"):
    st.session_state.message = "Investment Insights: Most deals are in the 0-50 lakh range!"
if col2.button("Show Top Investors"):
    st.session_state.message = "Top Investors: Aman and Peyush have invested in the most deals!"
if col3.button("Show Success Rate"):
    st.session_state.message = f"Success Rate: {(df['deal'].sum() / len(df) * 100):.2f}% of pitches received funding!"

st.subheader(st.session_state.message)

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
