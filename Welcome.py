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
    col = ['Name','Email','Time','Comment']
    spread.df_to_sheet(dataframe[col],sheet=spreadsheetname,index=False)
    st.sidebar.info('Comment Submmitted!')


st.title('Welcome to More Information')

st.sidebar.success("Select a page to visit")

st.markdown("""    
            ## I am pleased you've decided to scan my QR code. In this page you will find extra information about the topic and poster.
            Please use the pages on left of the screen to navigate or follow the links below. I'd be thrilled if you leave comments and/or feddbacks.

            ### About the Poster
            - View the poster by simply clicking the page 'Poster' or [click here](https://j-alex-vindel-bi-level-conference23.streamlit.app/Poster)
            - Check out a quick explanation video at the 'Video' page or [here](https://j-alex-vindel-bi-level-conference23.streamlit.app/Video)
            
            """)

st.divider()
st.markdown("""
#### Leave a Comment
  """)
input_name = st.text_input('Name',"")
input_mail = st.text_input('Mail (optional)')
input_text = st.text_area('Enter text',"")
st.caption('Comments will be saved and checked')

button = st.button('Submit')

if button:
    opt = {'Name':[input_name],
            'Email':[input_mail],
            'Time':[datetime.now()],
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
    #### To Submit add name and comment
    """)

st.divider()
st.markdown("""
           ### Want to know more aboute me?

            - Profile and social media links [Click Me](https://j-alex-vindel-bi-level-conference23.streamlit.app/About_Me)

            """)