# streamlit app for text processing, input a text, and display results

import streamlit as st
import numpy as np
import cv2

def process_text(text):
    return text+" processed "

st.title("Text Processing")

# prompt to upload image
img = st.file_uploader("Upload image here",type=['png','jpg','jpeg'])
brightness = st.slider('brightness',0.0,2.0,1.0)

if img:
    img = cv2.imdecode(np.frombuffer(img.getvalue(),np.uint8),cv2.IMREAD_COLOR) # decode image
    # show img
    img = np.array(img*brightness,dtype=np.uint8)

    st.image(img)


text = st.text_area("Input text here")
if st.button("Process"):
    result = process_text(text)

