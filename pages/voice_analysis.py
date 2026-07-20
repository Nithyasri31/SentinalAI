import streamlit as st
from utils.speech_utils import speech_to_text
from utils.gemini_utils import analyze_text

st.title("🎤 Voice Scam Detector")

st.write(
    "Upload an audio recording to detect whether it contains signs of a scam."
)

uploaded_file = st.file_uploader(
    "Upload an audio file",
    type=["mp3", "wav", "m4a", "mp4"]
)

if uploaded_file:

    # Save uploaded file
    with open("uploads/audio/temp.mp3", "wb") as f:
        f.write(uploaded_file.read())

    st.success("✅ Audio uploaded successfully!")

    st.divider()

    # Speech to Text
    st.subheader("📝 Transcript")

    with st.spinner("Converting speech to text..."):
        transcript = speech_to_text("uploads/audio/temp.mp3")

    st.caption("Speech Converted to Text")
    st.text_area(
        "",
        transcript,
        height=150,
        disabled=True
    )

    st.divider()

    # Gemini Analysis
    st.subheader("🤖 Scam Analysis")

    try:
        with st.spinner("Analyzing transcript with Gemini..."):
            result = analyze_text(transcript)

        st.success("Analysis Complete")

        st.markdown(result)

    except Exception as e:
        st.warning(
            """
⚠️ Gemini API quota has been exceeded or is temporarily unavailable.

Speech-to-Text is working correctly.

Scam analysis will work again once:
- The Gemini quota resets
- OR a new API key is used
- OR billing is enabled
"""
        )

        # Optional: show the actual error for debugging
        with st.expander("Show Error Details"):
            st.code(str(e))