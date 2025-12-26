import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ""

# Load environment variables
load_dotenv()

# Configure Gemini API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.set_page_config(page_title="Himanshu Chatbot", page_icon="")
st.title("AI Chatbot")
st.write("Chat with model in real time!")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Create chatbot model
model = genai.GenerativeModel("gemini-2.5-flash")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Type your message here...")

if prompt:
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    try:
        response = model.generate_content(prompt)
        reply = response.text

        with st.chat_message("assistant"):
            st.markdown(reply)

        st.session_state.messages.append({"role": "assistant", "content": reply})

    except Exception as e:
        st.error(f"Error: {e}")
