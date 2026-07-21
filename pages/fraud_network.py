import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

from utils.graph_utils import (
    create_graph,
    draw_graph,
    network_statistics,
    top_connected_nodes
)

st.set_page_config(page_title="Fraud Network", layout="wide")

st.title("🌐 Fraud Network Analysis")
st.markdown("### Connected Phone Numbers & UPI IDs")

# Load Data
df = pd.read_csv("data/sample_transactions.csv")

# Sidebar
option = st.sidebar.radio(
    "View",
    ["All Transactions", "Fraud Transactions"]
)

if option == "Fraud Transactions":
    df = df[df["Fraud"] == "Yes"]

# Create Graph
G = create_graph(df)

# Graph
st.pyplot(draw_graph(G))

# Network Statistics
stats = network_statistics(G)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Nodes", stats["Nodes"])
col2.metric("Edges", stats["Edges"])
col3.metric("Components", stats["Connected Components"])
col4.metric("Avg Degree", stats["Average Degree"])

# Most Connected Accounts
st.subheader("🔥 Most Connected Accounts")

top = top_connected_nodes(G)

top_df = pd.DataFrame(
    top,
    columns=["Phone / UPI", "Connections"]
)

st.dataframe(top_df, use_container_width=True)

# Connected Transactions
st.subheader("📋 Connected Transactions")

st.dataframe(
    df[
        [
            "Transaction_ID",
            "Phone",
            "UPI",
            "Amount",
            "Fraud"
        ]
    ],
    use_container_width=True
)

# Download
csv = df.to_csv(index=False).encode()

st.download_button(
    "📥 Download Network Report",
    csv,
    "fraud_network.csv",
    "text/csv"
)