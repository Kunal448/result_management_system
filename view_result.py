import streamlit as st
import pandas as pd
import time
from streamlit_gsheets import GSheetsConnection

def page3():
    url = "https://docs.google.com/spreadsheets/d/1Bd7iDW_uNA-ttIMYgtsFBs7fFlx-Yzq9DEMCdPNKFxg/edit?usp=sharing"
    conn = st.connection("gsheets", type = GSheetsConnection)
    
    data = conn.read(worksheet="Sheet1", ttl=3)
    df = pd.DataFrame(data)
    
    st.title("View Result")
    roll = st.text_input("Enter Roll No: ", int(1))
    roll_int = int(roll)
    condition = df['RollNo'] == roll_int
    row = df[condition]
    
    view_result = st.button("View Result", type="primary")
    
    if view_result:
        if roll_int in df['RollNo'].values:        
            for column in row['RollNo']:
                if column != roll_int:
                    time.sleep(1)
                else:                
                    sr_no, roll_no = st.columns(2)
                    with sr_no:
                        sr_no1 = st.text_input("Serial Number", int(row['SrNo'][roll_int-1]))
                        sr_no_int = int(sr_no1)
                    with roll_no:
                        roll_no1 = st.text_input("Roll No: ", int(row['RollNo'][roll_int-1]))
                        roll_no_int = int(roll_no1)                    
                    
                    st.subheader("Students Details")
                    name, email = st.columns([1,2])    
                    with name:
                        name1 = st.text_input("Name", str(row['Name'][roll_int-1]))
                        name_str = str(name1)
                    with email:
                        email1 = st.text_input("Email ID", str(row['Email'][roll_int-1]))
                        email_str = str(email1)
                    
                    st.subheader("Marks Details")
                    english, hindi, maths = st.columns([1,1,1])    
                    with english:
                        english1 = st.text_input("English", int(row['English'][roll_int-1]))
                        english_int = int(english1) 
                    with hindi:
                        hindi1 = st.text_input("Hindi", int(row['Hindi'][roll_int-1]))
                        hindi_int = int(hindi1)
                    with maths:
                        maths1 = st.text_input("Maths", int(row['Maths'][roll_int-1]))
                        maths_int = int(maths1)
                        
                    ss, science = st.columns([1,1])
                    with ss:
                        ss1 = st.text_input("Social Science", int(row['SS'][roll_int-1]))
                        ss_int = int(ss1)
                    with science:
                        science1 = st.text_input("Science", int(row['Science'][roll_int-1]))
                        science_int = int(science1)                           
                        
                    st.subheader("Overall Result")
                    total, percentage = st.columns([1,1])
                    with total:
                        total1 = st.text_input("Total",int(row['Total'][roll_int-1]))
                        total_int = int(total1)
                    with percentage:
                        percentage1 = st.text_input("Percentage", float(row['Percentage'][roll_int-1]))
                        percentage_float = float(percentage1)
                    
                    grade, result = st.columns([1,1])
                    with grade:
                        grade1 = st.text_input("Grade", str(row['Grade'][roll_int-1]))
                        grade_str = str(grade1)
                    with result:
                        result1 = st.text_input("Result", str(row['Result'][roll_int-1]))
                        result_str = str(result1)
                        
        else:
            st.warning("Result Doesn't Exists")