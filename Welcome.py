import streamlit as st

st.title('Welcome to More Information')

st.sidebar.success("Select a page to visit")

st.markdown("""    
            ## I am pleased you've decided to scan my QR code. In this page you will find extra information about the topic and poster.
            Please use the pages on left of the screen to navigate or follow the links below. I'd be thrilled if you leave comments and/or feddbacks.

            ### Information About Poster
            - View the poster by simply clicking the page 'Poster' or [click here](https://j-alex-vindel-bi-level-conference23.streamlit.app/Poster)
            - Check out a quick explanation video at the 'Video' page or [here](https://j-alex-vindel-bi-level-conference23.streamlit.app/Video)
            
            """)

st.divider()
st.markdown("""
#### Leave a Comment
  """)
input_name = st.text_input('Name')
input_mail = st.text_input('Mail (optional)')
input_text = st.text_area('Enter text')
st.caption('Comments will be saved and checked')

if st.button('Submit'):
    st.write(input_text)
    st.success('Your comment has been submitted, Thank you!', icon="✅")
    st.balloons()


st.divider()
st.markdown("""
           ### Want to know more aboute me?

            - Profile and social media links [Click Me](https://j-alex-vindel-bi-level-conference23.streamlit.app/About_Me)

            """)