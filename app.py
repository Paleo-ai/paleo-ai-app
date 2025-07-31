# app.py
import streamlit as st
from modules.chatbot import respond

st.set_page_config(page_title="AI Asistent - Rozpoznávání mincí")

st.title("🧠 AI Asistent pro rozpoznání mincí")
st.write("Zeptej se mě na cokoliv nebo mi pošli fotku mince!")

# Chat vstup
user_input = st.text_input("💬 Tvoje zpráva:")

if user_input:
    response = respond(user_input)
    st.markdown(f"**🤖 Odpověď:** {response}")
