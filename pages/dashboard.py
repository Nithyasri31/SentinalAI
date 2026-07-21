import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Fraud Dashboard", layout="wide")

# Load Data
df = pd.read_csv("data/sample_transactions.csv")

st.title("🚨 SentinelAI Fraud Dashboard")
st.markdown("### Financial Fraud Monitoring System")

# Sidebar
status = st.sidebar.selectbox(
    "Fraud Status",
    ["All", "Yes", "No"]
)

if status != "All":
    df = df[df["Fraud"] == status]

# KPI Cards
total = len(df)
fraud = len(df[df["Fraud"] == "Yes"])
safe = total - fraud
amount = df["Amount"].sum()

c1, c2, c3, c4 = st.columns(4)

c1.metric("Transactions", total)
c2.metric("Frauds", fraud)
c3.metric("Safe", safe)
c4.metric("Amount", f"₹{amount:,}")

# Charts
col1, col2 = st.columns(2)

with col1:
    fig = px.pie(
        df,
        names="Fraud",
        hole=0.5,
        title="Fraud Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.bar(
        df.groupby("Bank")["Amount"].sum().reset_index(),
        x="Bank",
        y="Amount",
        color="Bank",
        title="Amount by Bank"
    )
    st.plotly_chart(fig, use_container_width=True)

# Line Chart
st.subheader("Transaction Trend")

fig = px.line(
    df,
    x="Date",
    y="Amount",
    color="Fraud",
    markers=True
)

st.plotly_chart(fig, use_container_width=True)

# Highest Fraud Transactions
st.subheader("🚨 Top Fraud Transactions")

fraud_df = df[df["Fraud"] == "Yes"]

st.dataframe(
    fraud_df.sort_values(
        "Amount",
        ascending=False
    ).head(5),
    use_container_width=True
)

# Download
csv = df.to_csv(index=False).encode()

st.download_button(
    "📥 Download Report",
    csv,
    "fraud_report.csv",
    "text/csv"
)