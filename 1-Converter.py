# my_streamlit_app.py
import streamlit as st
from unidecode import unidecode_expect_ascii

def count_bytes(text, encoding='utf-8'):
    return len(text.encode(encoding))

# Title
st.title('Unicode to ASCII text cleaner')

# Text input
user_input = st.text_area("Enter/paste your text here")

# Process text
if user_input:
    cleaned_text = unidecode_expect_ascii(user_input)
    st.write("Your text had", count_bytes(user_input), "bytes")
    st.write("""Here's the clean version of your text:  
    You can select all the text to copy it. """)
    st.text_area("Cleaned Text", cleaned_text, height=150)
    st.write("It now has", count_bytes(cleaned_text), "bytes")
