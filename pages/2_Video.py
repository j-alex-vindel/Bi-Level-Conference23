import streamlit as st
from datetime import datetime
import pandas as pd
from gspread_pandas import Spread,Client
from google.oauth2 import service_account

scope = [
'https://www.googleapis.com/auth/spreadsheets',
'https://www.googleapis.com/auth/drive'
]

credentials = service_account.Credentials.from_service_account_info(
                st.secrets["gcp_service_account"], scopes = scope)


client = Client(scope=scope,creds=credentials)
spreadsheetname = "Comments"
spread = Spread(spreadsheetname,client = client)

sh = client.open(spreadsheetname)

def load_spreadsheet(spreadsheetname):
    worksheet = sh.worksheet(spreadsheetname)
    df = pd.DataFrame(worksheet.get_all_records())
    return df

def update_spreadsheet(spreadsheetname,dataframe):
    col = ['Name','Email','Time','Section','Comment']
    spread.df_to_sheet(dataframe[col],sheet=spreadsheetname,index=False)
    st.sidebar.info('Comment Submmitted!')

st.markdown("""
            ## :blue[Video] 
            """)

videofile = open('pages/Pics/ICBO_Video(1).mp4','rb')
video_bytes = videofile.read()
st.video(video_bytes)

st.divider()
st.markdown("""
#### :memo:  Leave a Comment
  """)

with st.form('Comments',clear_on_submit=True):
    input_name = st.text_input('Name',"")
    input_mail = st.text_input('Mail (optional)')
    input_text = st.text_area('Enter text',"")
    st.caption('Comments will be saved and checked')

    button = st.form_submit_button('Submit')

if button:
    opt = {'Name':[input_name],
            'Email':[input_mail],
            'Time':[datetime.now()],
            'Section':['Video'],
            'Comment':[input_text]}
    opt_df = pd.DataFrame(opt)
    df = load_spreadsheet('Coms')
    newdf = df.append(opt_df,ignore_index=True)
    
    if opt['Name'][0] != '':
        update_spreadsheet('Coms',newdf)
        st.success(f'{input_name} your comment has been recorded, Thank you!', icon="✅")
    else:
        st.error('Please add a name', icon="🚨")
else:
    st.markdown("""
    #### Add name and comment to submit
    """)

st.divider()



st.divider()
st.markdown("""
            - #### :back: [Welcome page](https://j-alex-vindel-bi-level-conference23.streamlit.app/Welcome)
            - #### :frame_with_picture: [Poster](https://j-alex-vindel-bi-level-conference23.streamlit.app/Poster)
            - #### :bust_in_silhouette: [Profile and social media](https://j-alex-vindel-bi-level-conference23.streamlit.app/About_Me)

                """)