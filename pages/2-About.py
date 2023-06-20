import streamlit as st

st.set_page_config(page_title = "About", page_icon = "🧊", layout = "centered", initial_sidebar_state = "auto")

st.title("Unicode to ASCII converter")

st.write("""This is a simple open-source app converts Unicode text to ASCII text.  
Fixes text that are too long because of special characters.  
This does not work with emojis and other languages.  """)

st.markdown("The github repo for this app can be found [here!](https://github.com/wheynelau/simple-unidecoder)")
