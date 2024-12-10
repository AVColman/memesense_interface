import streamlit as st
import streamlit.components.v1 as components  # Import Streamlit

st.set_page_config(
            page_title="MemeSense",
            page_icon=":performing_arts:", #Change icon later
            layout="wide", # or centered, wide has more space
            initial_sidebar_state="auto") # collapsed

st.write("# Welcome to MemeSense! 👋")

st.sidebar.success("Select an app above")

st.write("#### MemeSense is a project that classifies memes between the following categories: Positive, Negative and Neutral")

st.write("")

st.write("")
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)



meme_text = st.text_input('Meme text', 'Nom puemde ser')

st.write("")

st.write("")

st.write("")

st.write("")

st.write("")

st.write("")

st.write("")

st.write("")

st.write("")

st.write("")

st.write("")

st.write("")
