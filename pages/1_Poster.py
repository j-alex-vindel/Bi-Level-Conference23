import streamlit as st
from PIL import Image


st.markdown("""
            ## :purple[Poster] 
            """)

image = Image.open('pages/Pics/poster_dsms2023.jpg')

st.image(image,caption='Poster')

st.divider()

st.markdown("""
            - #### :back: [Welcome page](https://j-alex-vindel-bi-level-conference23.streamlit.app/Welcome)
            - #### :film_frames: [Video](https://j-alex-vindel-bi-level-conference23.streamlit.app/Video)
            - #### :bust_in_silhouette: [Profile and social media](https://j-alex-vindel-bi-level-conference23.streamlit.app/About_Me)

                """)