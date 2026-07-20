import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-3.5-flash")


def analyze_text(text):

    prompt = f"""
You are an AI Voice Scam Detector.

Analyze the following transcript.

Transcript:
{text}

Respond ONLY in this format:

Risk Level: High / Medium / Low

Reason:
(Explain why)

Suggestion:
(Explain what the user should do)
"""

    response = model.generate_content(prompt)

    return response.text