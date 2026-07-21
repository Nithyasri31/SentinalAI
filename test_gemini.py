from dotenv import load_dotenv
load_dotenv()

import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-3.5-flash")
response = model.generate_content("Say Hello")

print(response.text)