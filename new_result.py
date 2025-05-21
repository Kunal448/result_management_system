import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

def page2():
    global total_int, percentage_float, grade_str, result_str
    
    styling = """
    <style>
    [data-testid="stButton"] {
        text-align: center;
    }
    </style>
    """
    st.markdown(styling, unsafe_allow_html=True)

    url = "https://docs.google.com/spreadsheets/d/1Bd7iDW_uNA-ttIMYgtsFBs7fFlx-Yzq9DEMCdPNKFxg/edit?usp=sharing"
    conn = st.connection("gsheets", type = GSheetsConnection)
    
    data = conn.read(worksheet="Sheet1", ttl=3)
    df = pd.DataFrame(data)
    
    maximum = df['SrNo'].max()

    st.title("New Result")
    sr_no, roll_no = st.columns(2)
    with sr_no:
        sr_no1 = st.text_input("Serial Number", int(int(maximum) + 1))
        sr_no_int = int(sr_no1)
    with roll_no:
        roll_no1 = st.text_input("Enter Roll No: ", int())
        roll_no_int = int(roll_no1)
    st.subheader("Enter Students Details")
    name, email = st.columns([1,2])    
    with name:
        name1 = st.text_input("Name", str())
        name_str = str(name1)
    with email:
        email1 = st.text_input("Email ID", str())
        email_str = str(email1)
    
    st.subheader("Enter Marks Details")
    english, hindi, maths = st.columns([1,1,1])    
    with english:
        english1 = st.text_input("English", int())
        english_int = int(english1) 
    with hindi:
        hindi1 = st.text_input("Hindi", int())
        hindi_int = int(hindi1)
    with maths:
        maths1 = st.text_input("Maths", int())
        maths_int = int(maths1)
        
    ss, science = st.columns([1,1])
    with ss:
        ss1 = st.text_input("Social Science", int())
        ss_int = int(ss1)
    with science:
        science1 = st.text_input("Science", int())
        science_int = int(science1)
        
    calculate = st.button("Calculate Result", type="primary")
    
    if calculate:
        if sr_no_int != roll_no_int:
            st.warning("SrNo and Roll Number should be same")
        elif name_str == "":
            st.warning("Name Field Should Not Be Empty")
        elif email_str == "":
            st.warning("Email Field Should Not Be Empty")
        elif (english_int <0 or english_int >100):
            st.warning("Marks Should be from 0 to 100")
        elif (hindi_int <0 or hindi_int >100):
            st.warning("Marks Should be from 0 to 100")
        elif (maths_int <0 or maths_int >100):
            st.warning("Marks Should be from 0 to 100")
        elif (ss_int <0 or ss_int >100):
            st.warning("Marks Should be from 0 to 100")
        elif (science_int <0 or science_int >100):
            st.warning("Marks Should be from 0 to 100")    
        else:
            #conditions for input fields        
            st.subheader("Calculated Result")
            total, percentage = st.columns([1,1])
            with total:
                total1 = st.text_input("Total",int(english_int + hindi_int + maths_int + ss_int + science_int))
                total_int = int(total1)
            with percentage:
                percentage1 = st.text_input("Percentage", float((int(english_int + hindi_int + maths_int + ss_int + science_int)*100)/500))
                percentage_float = float(percentage1)
                
            g = ""
            r = ""
            
            if percentage_float>=91 and percentage_float<100:
                g = "A"
                r = "PASS"
            elif percentage_float>=81 and percentage_float<=90:
                g = "B"
                r = "PASS"
            elif percentage_float>=71 and percentage_float<=80:
                g = "C"
                r = "PASS"
            elif percentage_float>=61 and percentage_float<=70:
                g = "D"
                r = "PASS"
            elif percentage_float>=51 and percentage_float<=60:
                g = "E"
                r = "PASS"
            elif percentage_float>=41 and percentage_float<=50:
                g = "F"
                r = "PASS"
            else:
                g = "F"
                r = "FAIL"
            
            grade, result = st.columns([1,1])
            with grade:
                grade1 = st.text_input("Grade", g)
                grade_str = str(grade1)
            with result:
                result1 = st.text_input("Result", r)
                result_str = str(result1)
            
    save_result = st.button("Save Result")
    
    if save_result:            
        existing_data = conn.read(worksheet="Sheet1", usecols=list(range(13)), ttl=3)
        existing_data = existing_data.dropna(how="all")
            
        result_data = pd.DataFrame(
            [
                {
                    "SrNo": sr_no_int,
                    "RollNo": roll_no_int,
                    "Name": name_str,
                    "Email": email_str,
                    "English": english_int,
                    "Hindi": hindi_int, 
                    "Maths": maths_int,
                    "SS": ss_int,
                    "Science": science_int,
                    "Total": total_int,
                    "Percentage": percentage_float,
                    "Grade": grade_str,
                    "Result": result_str,
                }
            ]
        )
        
        updated_df = pd.concat([existing_data, result_data], ignore_index=True)
        
        conn.update(worksheet="Sheet1", data=updated_df)
        
        st.success("Result Saved Successfully")