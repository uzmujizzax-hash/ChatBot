import os
from ollama import Client
import streamlit as st  
client = Client(
    host=st.secrets["HOST"],
    headers={'Authorization': f'Bearer {st.secrets["OLLAMA_API_KEY"]}'}
)

st.markdown("## :rainbow[O'zbekiston Milliy universitetining Jizzax filiali bot yordamchisi]")

xabar = st.chat_input("Savolingizni kiriting:")

if xabar:
    st.write(xabar)
    placeholder = st.empty()
    response_text = ""
    messages = [
    {
        'role': 'user',
        'content': xabar+st.secrets["SETUP_PROMPT"]
    },
    ]
    with st.spinner('Tez orada savolingizga javob beramiz...'):
        for part in client.chat(st.secrets['MODEL'], messages=messages, stream=True):
            response_text += part['message']['content']
            placeholder.markdown(response_text, unsafe_allow_html=True)
