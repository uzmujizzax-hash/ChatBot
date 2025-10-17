import os
from ollama import Client
import streamlit as st  
client = Client(
    host="https://ollama.com",
    headers={'Authorization': f'Bearer {st.secrets["OLLAMA_API_KEY"]}'}
)

st.markdown("## :rainbow[O'znbekistan Milliy universitetining Jizzax filiali bot yordamchisi]")


xabar = st.chat_input("Savolingizni kiriting:")

setup_prompt="""
Qoidalar:
Istalgan xabar yozilsa sen o'zingni "Men O'zbekiston Milliy universitetining Jizzax filiali bot yordamchisiman deb ayt. Savollaringizga yordam berishga tayyorman deb aytishing kerak."
Sen o'zingni modelingni so'ralgan harqanday javobga javob bermasliging kerak
"""
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
        'content': xabar+setup_prompt,
    },
    ]
    with st.spinner('Tez orada savolingizga javob beramiz...'):
        for part in client.chat('gpt-oss:120b', messages=messages, stream=True):
            response_text += part['message']['content']
            placeholder.markdown(response_text)