# app/streamlit_app.py

import streamlit as st
from agent import ask_agent
from PIL import Image

st.set_page_config(page_title="Customer Support AI", page_icon="🤖", layout="centered")

# Load logo
logo = Image.open("app/support ai.png")  # Move the logo we made into app
st.image(logo, width=200)

st.title("Customer Support AI 🛒")

st.markdown("""
<style>
    .main {
        background-color: #F0F2F6;
    }
    h1 {
        color: #0D3B66;
        font-family: 'Arial';
    }
</style>
""", unsafe_allow_html=True)

question = st.text_input("Ask about your order:")

if st.button("Submit"):
    if question:
        with st.spinner('Thinking...'):
            response = ask_agent(question)
        st.success(response)
    else:
        st.warning("Please ask a question about your order.")
