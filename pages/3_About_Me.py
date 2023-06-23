import streamlit as st
from PIL import Image


st.markdown("""
            ## :blue[About Me] 
            """)

st.markdown("""
            - #### 👋 Hi, I’m Alexander Vindel a PhD student at Strathclyde University in the Business School in the Management Science Department
            - #### 👀 My research interests are in mathematical optimization, linear programming, integer programming, network optimization, bi-level programming and data analytics
            - #### 🌱 I mostly work with Python and Gurobi
            - #### :bulb: I’d be interested in collaborating on integer programming and operations research as a whole
            - #### 📫 Reach me by email at (jose.vindel-garduno@strath.ac.uk) | (alexander.vindel@gmail.com) or check my social networks below

            """)



st.divider()

st.header('Social Media')

col1,col2 = st.columns(2,gap='medium')

with col1:
    
    linkedin = Image.open('pages/Pics/linkedin.png')

    st.image(linkedin,caption='LinkedIn',output_format='PNG')
    st.markdown('### [**alexander-vindel**](https://www.linkedin.com/in/alexander-vindel/)')

with col2:
    
    github = Image.open('pages/Pics/github.png')

    st.image(github,caption='Github',output_format='PNG')
    st.markdown('### [**j-alex-vindel**](https://github.com/j-alex-vindel)')

with st.expander('''Icon's Credits'''):
    st.caption('''https://www.flaticon.com/free-icons/linkedin''')
    st.caption('''https://www.flaticon.com/free-icons/github''')

st.divider()

st.markdown("""
            - #### :back: [Welcome page](https://j-alex-vindel-bi-level-conference23.streamlit.app/Welcome)
            - #### :film_frames: [Video](https://j-alex-vindel-bi-level-conference23.streamlit.app/Video)
            - #### :frame_with_picture: [Poster](https://j-alex-vindel-bi-level-conference23.streamlit.app/Poster)

                """)