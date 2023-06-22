import streamlit as st

st.title('Welcome to More Information')

st.sidebar.success("Select a page to visit")

st.markdown("""    
            ## I am pleased you've decided to scan my QR code. In this page you will find extra information about the topic and poster.
            Please use the pages on left of the screen to navigate or follow the links below. I'd be thrilled to have comments and/or feddbacks.

            ### Information About Poster
            - View the poster by simply clicking the page 'Poster' or [click here](https://j-alex-vindel-bi-level-conference23.streamlit.app/Poster)
            - Check out a quick explanation video at the 'Video' page or [here](https://j-alex-vindel-bi-level-conference23.streamlit.app/Video)
            
            
            #### Want to know more aboute me?
            - Profile and social media links [Click Me](https://j-alex-vindel-bi-level-conference23.streamlit.app/About_Me)


            """)

st.divider()
st.markdown("""
#### Leave a Comment - click the button
  """)

input_text = st.text_area('Enter text')

if st.button('Leave a Comment'):
    st.write(input_text)