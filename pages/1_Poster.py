import streamlit as st
from PIL import Image


st.write('Poster')

image = Image.open('pages/Pics/poster_dsms2023.jpg')

st.image(image,caption='Poster')