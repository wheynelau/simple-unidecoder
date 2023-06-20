# my_streamlit_app.py
import streamlit as st
from unidecode import unidecode_expect_ascii

def count_bytes(text, encoding='utf-8'):
    return len(text.encode(encoding))
st.set_page_config(
    page_title="Text cleaner",
    page_icon=":hippopotamus:",
    layout="wide",
    initial_sidebar_state="expanded",
)
# Title
st.title('Unicode to ASCII text cleaner')

# Text input
user_input = st.text_area("Enter/paste your text here")

# Process text
if user_input:
    cleaned_text = unidecode_expect_ascii(user_input)
    st.write("Your text had", count_bytes(user_input), "bytes")
    font_col, text_col = st.columns(2)
    with font_col:
        font_options = ['Arial', 'Helvetica', 'Times New Roman', 'Courier New', 'Verdana', 'Georgia']
        font = st.selectbox('Select your font:', font_options)

    with text_col:
        text_size = st.number_input('Select your font size:', min_value=1,
         max_value=100, value=12, step=1)
    st.write("""Here's the clean version of your text:  
    You can select all the text to copy it. """)
    no_breaks= cleaned_text.replace('\n', '<br>')
    output_text = f'<p style="font-family:{font}; font-size: {text_size}px;">{no_breaks}</p>'

    st.markdown(output_text, unsafe_allow_html=True)
    st.write("It now has", count_bytes(cleaned_text), "bytes")
