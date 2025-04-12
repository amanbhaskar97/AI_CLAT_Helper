import streamlit as st
from gemini_chatbot import GeminiChatbot

# Initialize chatbot
bot = GeminiChatbot(data_dir="data")

st.title("CLAT Legal Exam Chatbot")

query = st.text_input("Ask your CLAT-related question:")

if query:
    response = bot.get_answer(query)
    st.write("**Answer:**")
    st.success(response)
