import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

def page6():
    url = "https://docs.google.com/spreadsheets/d/1Bd7iDW_uNA-ttIMYgtsFBs7fFlx-Yzq9DEMCdPNKFxg/edit?usp=sharing"
    conn = st.connection("gsheets", type = GSheetsConnection)
    
    data = conn.read(worksheet="Sheet1", ttl=3)
    df = pd.DataFrame(data)
    
    st.title("Delete Result")
    
    roll_no = st.text_input("Enter Roll Number: ", int())
    roll_no_int = int(roll_no)
    
    delete_result = st.button("Delete Result", type="primary")
    
    if delete_result:
        if roll_no_int in df['RollNo'].values:
            condition = df['RollNo'] == roll_no_int
            
            df = df[~condition]
            
            conn.update(worksheet="Sheet1", data=df)
            
            st.success("Result Successfully Deleted")
        else:
            st.warning("Result Doesn't Exist")