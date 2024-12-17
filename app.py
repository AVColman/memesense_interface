import streamlit as st
import streamlit.components.v1 as components  # Import Streamlit
import requests
#import cv2
#import pytesseract
#from io import StringIO
from PIL import Image
import numpy as np


API_URL = "http://127.0.0.1:8000/predict/"

st.set_page_config(
            page_title="MemeSense",
            page_icon=":performing_arts:", #Change icon later
            layout="wide", # or centered, wide has more space
            initial_sidebar_state="auto") # collapsed

CSS = """
<style>
/* Background for the entire page */
[data-testid="stAppViewContainer"] {
background: rgb(24,4,33);
background: linear-gradient(0deg, rgba(24,4,33,1) 0%, rgba(127,61,148,1) 100%);
}

/* Keep text styles unaffected */
h1 {
    text-shadow: 4px 2px 6px #9aa19b;
}
</style>
"""

# Apply CSS to the page
st.markdown(CSS, unsafe_allow_html=True)



st.write("# Welcome to MemeSense! 👋")

st.write("##")

### gif from url
st.markdown("![Alt Text](https://i.gifer.com/Fh5.gif)")

#Proyect Description
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:

        st.header("What is MemeSense?")

        st.write("##")

        st.write("#### MemeSense is a DeepLearning project that classifies memes between Positive and Negative.")

        st.write("##")

        st.header("What is it for?")

        st.write("##")

        st.write("#### It can be used to apply a meme filter if you don't want to see negative memes on your page.")

        st.write("#### It can help you interpret whether a meme is negative or positive if you are not versed in the world of memes.")

with right_column:

    st.write("##")

    st.markdown("![Alt Text](https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExcTlyeWNtamYzMGkweG9mZTc0MXgyOGIyNGFrYzY2aXBwNXpxcHNnbiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/WRQBXSCnEFJIuxktnw/giphy.webp)")


st.write("##")

st.write("---")

st.write("##")

#User explanation
st.header("How it works?")

st.write("#### You just need to upload the meme you want to analyse from your local folder and wait for our app to tell you the result! Supported formats are .jpg, .jpeg and .png.")

st.write("##")

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
        response = requests.post("http://127.0.0.1:8000/predict", files=files)

        if response.status_code == 200:
            st.write(f"API Response: {response.json()}")
            prediction = response.json()['label']

            if prediction == 0:
                label = "Negative"
                st.markdown("![Alt Text](https://i.gifer.com/5OQ.gif)")
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


#Altrnativa por si no corre el pytesseract:

# Text input for the string
#text_input = st.text_input("Enter the meme's text:")

#if st.button("Predict"):
#    if uploaded_file and text_input:
#        files = {"image": uploaded_file.getvalue()}
#        data = {"text": text_input}
#        response = requests.post("http://localhost:8000/upload_image", files=files, data=data)
#        if response.status_code == 200:
#            st.success("Request successful!")
#        else:
#            st.error("Request failed.")
#    else:
#        st.write("You need to enter an image and a text!") #ver si se puede distinguir entre imagen y texto faltante

 # Convert the image to gray scale
    #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Performing OTSU threshold
    #ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
    # Specify structure shape and kernel size.
    # Kernel size increases or decreases the area
    # of the rectangle to be detected.
    # A smaller value like (10, 10) will detect
    # each word instead of a sentence.
    #rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))
    # Applying dilation on the threshold image
    #dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
    # Finding contours
    #contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
   #                                              cv2.CHAIN_APPROX_NONE)
    # Creating a copy of image
    #im2 = img.copy()

    #Variable to save the text of the meme

    #texto = ""

# Looping through the identified contours
# Then rectangular part is cropped and passed on
# to pytesseract for extracting text from it
# Extracted text is then written into the text file
   # for cnt in contours:
   #     x, y, w, h = cv2.boundingRect(cnt)

    # Drawing a rectangle on copied image
   #     rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Cropping the text block for giving input to OCR
    #    cropped = im2[y:y + h, x:x + w]

    # Open the file in append mode
    #file = open("recognized.txt", "a")


    # Apply OCR on the cropped image
    #    text = pytesseract.image_to_string(cropped)

    # Appending the text into file
    #file.write(text)
    #file.write("\n")
    #    texto = texto + " " + text
