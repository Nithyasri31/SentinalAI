import streamlit as st
from pathlib import Path
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="SentinelAI",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Load CSS
def load_css():
    css = Path("assets/style.css")
    if css.exists():
        st.markdown(
            f"<style>{css.read_text()}</style>",
            unsafe_allow_html=True,
        )

load_css()

# ---------------------------
# Sidebar
# ---------------------------
with st.sidebar:

    st.image("assets/logo.png", width=280)

    st.markdown("# SentinelAI")

    st.caption("AI Powered Public Safety")

    st.divider()

    # st.page_link("app.py", label="🏠 Home")

    # st.page_link("pages/scam_detection.py",
    #              label="📩 Scam Detection")

    # st.page_link("pages/voice_analysis.py",
    #              label="🎤 Voice Analysis")

    # st.page_link("pages/dashboard.py",
    #              label="📊 Fraud Dashboard")

    # st.page_link("pages/fraud_network.py",
    #              label="🕸 Fraud Network")

    # st.divider()

    st.success("AI Intelligence Platform")

# ===========================
# Hero Section
# ===========================

left, right = st.columns([1.2, 1])

with left:

    st.markdown("""
    <h1 style='font-size:60px;line-height:1.1;'>
    AI-Powered Intelligence<br>
    for a <span style='color:#7CFC00;'>Safer Tomorrow</span>
    </h1>
    """, unsafe_allow_html=True)

    st.write("")

    st.markdown("""
    <h4 style='color:#d6d6d6;font-weight:400;line-height:1.8;'>

    Detect, analyze and prevent digital scams,
    financial fraud, counterfeit currency,
    digital arrest scams and cyber threats
    using AI-powered intelligence.

    </h4>
    """, unsafe_allow_html=True)

    # col1, col2 = st.columns(2)

    # with col1:
    #     st.button("🚀 Explore Modules", use_container_width=True)

    # with col2:
    #     st.button("📊 View Dashboard", use_container_width=True)

with right:

    st.image("assets/hero.png", use_container_width=True)

st.markdown("<br>", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Cybercrime Complaints",
        "1.14M+",
        "2023"
    )

with c2:
    st.metric(
        "Digital Arrest Fraud",
        "₹1776 Cr",
        "2024"
    )

with c3:
    st.metric(
        "Increase in Crime",
        "60%",
        "YoY"
    )

with c4:
    st.metric(
        "AI Monitoring",
        "24×7",
        "Real-Time"
    )

st.markdown("---")

st.markdown(
    "<h2 style='text-align:center;'>Our AI Modules</h2>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;color:gray;'>Powerful AI tools for Digital Public Safety</p>",
    unsafe_allow_html=True
)
st.write("")

m1, m2, m3, m4 = st.columns(4)

# -------------------------
# Scam Detection
# -------------------------
with m1:
    with st.container(border=True):

        st.subheader("📩 Scam Detection")

        st.write(
            "Detect scam SMS, phishing emails and malicious messages using AI-powered NLP."
        )

        st.markdown("""
        ✅ Scam / Genuine Prediction

        ✅ Scam Type Identification

        ✅ Risk Score Calculation

        ✅ Explain Why It's Suspicious
        """)

        # st.button("Explore Module", key="scam")

# -------------------------
# Voice Analysis
# -------------------------
with m2:
    with st.container(border=True):

        st.subheader("🎤 Voice Analysis")

        st.write(
            "Analyze suspicious phone calls using speech recognition and AI."
        )

        st.markdown("""
        ✅ Speech-to-Text

        ✅ AI Fraud Detection

        ✅ Scam Explanation

        ✅ Voice Pattern Analysis
        """)

        # st.button("Explore Module", key="voice")

# -------------------------
# Dashboard
# -------------------------
with m3:
    with st.container(border=True):

        st.subheader("📊 Fraud Dashboard")

        st.write(
            "Real-time fraud monitoring with analytics and visual insights."
        )

        st.markdown("""
        ✅ Fraud Statistics

        ✅ Transaction Trends

        ✅ Risk Analytics

        ✅ Live Monitoring
        """)

        # st.button("Explore Module", key="dashboard")

# -------------------------
# Network
# -------------------------
with m4:
    with st.container(border=True):

        st.subheader("🕸 Fraud Network")

        st.write(
            "Visualize relationships between suspicious entities and transactions."
        )

        st.markdown("""
        ✅ Entity Mapping

        ✅ UPI Connections

        ✅ Phone Number Analysis

        ✅ Fraud Network Graph
        """)

        # st.button("Explore Module", key="network")

st.markdown("---")

st.markdown(
    "<h2 style='text-align:center;'>Why SentinelAI?</h2>",
    unsafe_allow_html=True
)

st.write("")

a, b, c, d = st.columns(4)

with a:
    st.info("🧠\n\n### AI Powered\nAdvanced Machine Learning for accurate fraud detection.")

with b:
    st.info("🛡️\n\n### Secure\nEnd-to-End protection and secure data handling.")

with c:
    st.info("⚡\n\n### Real-Time\nInstant detection and intelligent threat monitoring.")

with d:
    st.info("👥\n\n### Built For Everyone\nCitizens, Banks and Law Enforcement Agencies.")

st.markdown("---")

st.markdown(
    "<h2 style='text-align:center;'>Built for ET AI Hackathon</h2>",
    unsafe_allow_html=True
)

st.markdown(
"""
Our platform integrates Artificial Intelligence,
Natural Language Processing,
Speech Intelligence,
Financial Fraud Analytics,
and Network Intelligence into a single Digital Public Safety Platform.

Designed to proactively detect Digital Arrest Scams,
Counterfeit Currency,
Financial Fraud,
Cybercrime,
and Organized Scam Networks.
"""
)

st.markdown("---")

st.markdown(
"""
<div style='text-align:center;color:gray;padding:20px;'>

<h2>🛡 SentinelAI</h2>

AI-Powered Public Safety Intelligence Platform

ET AI Hackathon 2026

Built with ❤️ using Python • Streamlit • Machine Learning • NLP

</div>
""",
unsafe_allow_html=True)