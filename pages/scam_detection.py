import streamlit as st
from utils.nlp_utils import predict_message

st.set_page_config(page_title="AI Scam Detector", page_icon="🛡️")

st.title("🛡️ AI Scam Detection")

st.write("Paste any SMS or Email below to check whether it is a scam.")

message = st.text_area(
    "Enter Message",
    height=200,
    placeholder="Paste SMS or Email here..."
)

if st.button("Analyze Message"):

    if message.strip() == "":
        st.warning("Please enter a message.")
    else:

        result = predict_message(message)

        if result["label"] == "Scam":
            st.error("🚨 Scam Detected")
        else:
            st.success("✅ Genuine Message")

        st.subheader("Prediction")

        st.write("**Label:**", result["label"])
        st.write("**Risk Score:**", f'{result["risk"]}%')
        st.write("**Scam Type:**", result["type"])

        st.subheader("Explanation")

        st.info(result["explanation"])