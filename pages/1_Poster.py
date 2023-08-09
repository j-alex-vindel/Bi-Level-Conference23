import streamlit as st
from PIL import Image
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
            ## :purple[Poster] 
            """)

image = Image.open('pages/Pics/poster_ICBO23(1).jpg')

st.image(image,caption='Poster')

st.divider()

st.markdown("""
            ## :purple[Model] 
            """)

col1,col2 = st.columns(2)

with col1:
    st.markdown("### Leader's ")
    st.latex(r'''
             
             \max~ \nu_{chemical}\\
             \sum(1-y_{j}) = K;~\forall j \in M\\
             
             ''')

with col2:
    
    st.markdown("### Follower's ")
    st.latex(r'''

       \max~ \nu_{growth}\\
        S_{ij} \cdot \nu_{j}=0;~\forall i \in N~ \forall j \in M\\
        \nu^{min}_{j} \cdot y_{j} \leq \nu_{j} \leq \nu^{max}_{j} \cdot y_{j};~\forall j \in M\\
         ''')


st.divider()
st.markdown("""
#### :memo: Leave a Comment
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
            'Section':['Poster'],
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





st.markdown("""
            - #### :back: [Welcome page](https://j-alex-vindel-bi-level-conference23.streamlit.app/Welcome)
            - #### :film_frames: [Video](https://j-alex-vindel-bi-level-conference23.streamlit.app/Video)
            - #### :bust_in_silhouette: [Profile and social media](https://j-alex-vindel-bi-level-conference23.streamlit.app/About_Me)

                """)