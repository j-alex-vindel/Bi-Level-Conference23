import streamlit as st
from PIL import Image


st.header('About Me')

st.divider()

st.header('Social Media')

col1,col2 = st.columns(2,gap='medium')

with col1:
    
    linkedin = Image.open('pages/Pics/linkedin.PNG')

    st.image(linkedin,caption='LinkedIn',output_format='PNG')
    st.markdown('## [**alexander-vindel**](https://www.linkedin.com/in/alexander-vindel/)')

with col2:
    
    github = Image.open('pages/Pics/github.PNG')

    st.image(github,caption='Github',output_format='PNG')
    st.markdown('## [**j-alex-vindel**](https://github.com/j-alex-vindel)')

with st.expander('''Icon's Credits'''):
    st.caption('''https://www.flaticon.com/free-icons/linkedin''')
    st.caption('''https://www.flaticon.com/free-icons/github''')