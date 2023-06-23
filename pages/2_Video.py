import streamlit as st

st.markdown("""
            ## :blue[Video] 
            """)

videofile = open('pages/Pics/video.mp4','rb')
video_bytes = videofile.read()
st.video(video_bytes)




st.divider()
st.markdown("""
            - #### :back: [Welcome page](https://j-alex-vindel-bi-level-conference23.streamlit.app/Welcome)
            - #### :frame_with_picture: [Poster](https://j-alex-vindel-bi-level-conference23.streamlit.app/Poster)
            - #### :bust_in_silhouette: [Profile and social media](https://j-alex-vindel-bi-level-conference23.streamlit.app/About_Me)

                """)