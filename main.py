import os
from ollama import Client
import streamlit as st  
client = Client(
    host="https://ollama.com",
    headers={'Authorization': 'Bearer ' + st.secrets["OLLAMA_API_KEY"]}
)

st.markdown("## :rainbow[Ollama va Streamlit bilan ChatGPT modeli]")
xabar = st.chat_input("Savolingizni kiriting:")

# uploaded_file = st.file_uploader("PDF faylni tanlang", type="pdf")
# if uploaded_file is not None:
#     st.pdf(uploaded_file, height=400)

if xabar:
    st.write(xabar)
    placeholder = st.empty()
    response_text = ""
    messages = [
    {
        'role': 'user',
        'content': xabar,
    },
    ]
    with st.spinner('Tez orada savolingizga javob beramiz...'):
        for part in client.chat('gpt-oss:120b', messages=messages, stream=True):
            response_text += part['message']['content']
            placeholder.markdown(response_text)