# my_streamlit_app.py
import streamlit as st
from unidecode import unidecode

def count_bytes(text, encoding='utf-8'):
    return len(text.encode(encoding))

# Title
st.title('Unicode to ASCII converter')

# Text input
user_input = st.text_area("Enter/paste your text here")

# Process text
if user_input:
    cleaned_text = unidecode(user_input)
    st.write("Your text had", count_bytes(user_input), "bytes")
    st.write("Here's the ASCII version of your text:")
    st.text(cleaned_text)
    st.write("It now has", count_bytes(cleaned_text), "bytes")

    # Add a button to allow copying to clipboard
    if st.button('Copy to clipboard'):
        st.copied_to_clipboard(cleaned_text)
