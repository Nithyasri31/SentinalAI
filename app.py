import streamlit as st
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="SentinelAI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------
# Sidebar
# ---------------------------
st.sidebar.title("🛡️ SentinelAI")
st.sidebar.markdown("### AI-Powered Public Safety & Fraud Prevention")

st.sidebar.success("Choose a module from the Pages menu.")

# ---------------------------
# Home Page
# ---------------------------
st.title("🛡️ SentinelAI")
st.subheader("AI-Powered Public Safety, Scam & Financial Fraud Prevention")

st.markdown("---")

st.markdown("""
Welcome to **SentinelAI**, an AI-powered platform designed to detect,
analyze, and prevent digital scams and financial fraud.

### Available Modules

📩 **Scam Detection**
- Detect scam SMS and emails
- Predict Scam / Genuine
- Identify scam type
- Calculate risk score
- Explain why the message is suspicious

🎤 **Voice Analysis**
- Upload suspicious audio
- Speech-to-text conversion
- AI-powered fraud analysis
- Scam explanation

📊 **Fraud Dashboard**
- Monitor fraud trends
- View fraud statistics
- Analyze transaction patterns
- Visualize fraud distribution
- Track suspicious transactions

🕸️ **Fraud Network**
- Visualize connections between suspicious entities
- Analyze connected phone numbers
- Track UPI ID relationships
- Identify potential fraud networks
- Explore suspicious transaction connections

---

### Team Modules

✅ NLP Scam Detection

✅ Voice Scam Analysis

✅ Financial Fraud Dashboard

✅ Fraud Network Analysis

More AI-powered safety modules can be added in future.
""")

st.info("👈 Select a module from the Pages section in the sidebar.")