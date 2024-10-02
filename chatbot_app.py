import os
import streamlit as st
import requests
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env file
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

def get_gemini_response(user_input):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(user_input)
    return response.text

st.title("Gemini Chatbot")

user_input = st.text_input("You:", "")

if user_input:
    bot_response = get_gemini_response(user_input)
    st.text_area("Gemini Bot:", value=bot_response, height=150)
