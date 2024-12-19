import streamlit as st
import streamlit.components.v1 as components
import requests
from PIL import Image
import numpy as np



API_URL = "http://127.0.0.1:8000/predict/"

#page configuration
st.set_page_config(
            page_title="MemeSense",
            page_icon=":performing_arts:", #Change icon later
            layout="wide", # or centered, wide has more space
            initial_sidebar_state="auto") # collapsed
#page background color
CSS = """
<style>
/* Background for the entire page */
[data-testid="stAppViewContainer"] {
background: rgb(24,4,33);
background: linear-gradient(0deg, rgba(24,4,33,1) 0%, rgba(100,176,222,1) 100%);
}

/* Keep text styles unaffected */
h1 {
    text-shadow: 4px 2px 6px #9aa19b;
}
</style>
"""

# Apply CSS to the page
st.markdown(CSS, unsafe_allow_html=True)



st.write("# 🎉 Welcome to MemeSense! 👋")

st.write("##")

### gif from url
#st.markdown("![Alt Text](https://i.gifer.com/Fh5.gif)")

#Proyect Description
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:

        st.header(" 📖 What is MemeSense?")

        st.write("##")

        st.write("#### MemeSense is a DeepLearning project that classifies memes between Positive and Negative.")

        st.write("##")

        st.header(" 🎯 What is it for?")

        st.write("##")

        st.write("#### 📌 Filter out negative memes if you don’t want to see them on your page.")

        st.write("#### 📌 Interpret the tone of a meme (positive or negative) if you’re not well-versed in meme culture.")

with right_column:

    st.write("##")

    st.markdown("![Alt Text](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExcTlyeWNtamYzMGkweG9mZTc0MXgyOGIyNGFrYzY2aXBwNXpxcHNnbiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/WRQBXSCnEFJIuxktnw/giphy.webp)")


st.write("##")

st.write("---")

st.write("##")

#User explanation
st.header("⚙️ How it works?")

st.write("#### 1. Upload a meme image from your local folder (supported formats: .jpg, .jpeg, .png)")

st.write("#### 2. Analyze the image with our model and wait for the result.")

st.write("##")

st.write("##")

st.write("---")

st.write("##")

st.header("🖼️ Try it out!")

st.write("##")


# File uploader for the image
uploaded_file = st.file_uploader("Choose an image in format jpg, png or jpeg...", type=["jpg", "png", "jpeg"])
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    #st.write(bytes_data)
    st.image(uploaded_file)

    # Read image from which text needs to be extracted
    image = Image.open(uploaded_file)
    #Convert the image to a Numpy array
    img = np.array(image)
    print(img.shape)


#Boton para enviar el archivo
if st.button("Predict"):
    if uploaded_file:
        files = {"image": uploaded_file.getvalue()}
        response = requests.post("https://memesense-app-383821638996.us-west1.run.app/predict", files=files)

        if response.status_code == 200:
            prediction = response.json()['label']

            if prediction == 0:
                label = "Negative"
                st.markdown("![Alt Text](https://i.gifer.com/5OQ.gif)")
                st.warning('Please consider the context and audience before sharing. Viewer discretion is advised.', icon="⚠️")
            elif prediction == 1:
                label = "Positive"
                st.markdown("![Alt Text](https://i.gifer.com/13ym.gif)")
            else:
                label = "Unknown"
                st.markdown("![Alt Text](https://i.gifer.com/fyhz.gif)")
            st.success(f"Prediction: {label}")
        else:
            st.error("Request failed.")
    else:
        st.write("You need to enter an image!")


st.write("##")

st.write("---")

st.write("##")

st. header(":mailbox: Get in touch with us!")

contact_form = """
<form action="https://formsubmit.co/alinavcolman@gmail.com" method="POST">
     <input type="text" name="name" Placeholder="Your name" required>
     <input type="email" name="email" Placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html= True)
