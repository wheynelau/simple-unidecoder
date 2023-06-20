# Import streamlit
import streamlit as st

# Read the contents of your README file
with open("README.md", "r") as f:
    readme_text = f.read()

# Display it using st.markdown
st.markdown(readme_text)    