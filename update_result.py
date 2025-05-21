import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection

def page5():
    global sr_no_int5, total_int5, percentage_float5, grade_str5, result_str5
    url = "https://docs.google.com/spreadsheets/d/1Bd7iDW_uNA-ttIMYgtsFBs7fFlx-Yzq9DEMCdPNKFxg/edit?usp=sharing"
    conn = st.connection("gsheets", type = GSheetsConnection)
    
    data = conn.read(worksheet="Sheet1", ttl=3)
    df = pd.DataFrame(data)
    
    st.title("Update Result")
    
    sr_no5, roll_no5 = st.columns(2)
    with sr_no5:
        sr_no5 = st.text_input("Serial Number", int(1))
        sr_no_int5 = int(sr_no5)
    with roll_no5:
        roll_no5 = st.text_input("Enter Roll No: ", int(1))
        roll_no_int5 = int(roll_no5)
    row = df[df['RollNo'] == roll_no_int5].iloc[0]
    st.subheader("Enter Students Details")
    name5, email5 = st.columns([1,2])    
    with name5:
        name5 = st.text_input("Name", row['Name'])
        name_str5 = str(name5)
    with email5:
        email5 = st.text_input("Email ID", row['Email'])
        email_str5 = str(email5)
    
    st.subheader("Enter Marks Details")
    english5, hindi5, maths5 = st.columns([1,1,1])    
    with english5:
        english5 = st.text_input("English", int(row["English"]))
        english_int5 = int(english5) 
    with hindi5:
        hindi5 = st.text_input("Hindi", int(row["Hindi"]))
        hindi_int5 = int(hindi5)
    with maths5:
        maths5 = st.text_input("Maths", int(row["Maths"]))
        maths_int5 = int(maths5)
        
    ss5, science5 = st.columns([1,1])
    with ss5:
        ss5 = st.text_input("Social Science", int(row["SS"]))
        ss_int5 = int(ss5)
    with science5:
        science5 = st.text_input("Science", int(row["Science"]))
        science_int5 = int(science5)
        
    calculate = st.button("Calculate Result", type="primary")
    
    if calculate:
        if sr_no_int5 != roll_no_int5:
            st.warning("SrNo and Roll Number should be same")
        elif name_str5 == "":
            st.warning("Name Field Should Not Be Empty")
        elif email_str5 == "":
            st.warning("Email Field Should Not Be Empty")
        elif (english_int5 <0 or english_int5 >100):
            st.warning("Marks Should be from 0 to 100")
        elif (hindi_int5 <0 or hindi_int5 >100):
            st.warning("Marks Should be from 0 to 100")
        elif (maths_int5 <0 or maths_int5 >100):
            st.warning("Marks Should be from 0 to 100")
        elif (ss_int5 <0 or ss_int5 >100):
            st.warning("Marks Should be from 0 to 100")
        elif (science_int5 <0 or science_int5 >100):
            st.warning("Marks Should be from 0 to 100")    
        else:
            #conditions for input fields        
            st.subheader("Calculated Result")
            total5, percentage5 = st.columns([1,1])
            with total5:
                total5 = st.text_input("Total",int(english_int5 + hindi_int5 + maths_int5 + ss_int5 + science_int5))
                total_int5 = int(total5)
            with percentage5:
                percentage5 = st.text_input("Percentage", float((int(english_int5 + hindi_int5 + maths_int5 + ss_int5 + science_int5)*100)/500))
                percentage_float5 = float(percentage5)
                
            g = ""
            r = ""
            
            if percentage_float5>=91 and percentage_float5<100:
                g = "A"
                r = "PASS"
            elif percentage_float5>=81 and percentage_float5<=90:
                g = "B"
                r = "PASS"
            elif percentage_float5>=71 and percentage_float5<=80:
                g = "C"
                r = "PASS"
            elif percentage_float5>=61 and percentage_float5<=70:
                g = "D"
                r = "PASS"
            elif percentage_float5>=51 and percentage_float5<=60:
                g = "E"
                r = "PASS"
            elif percentage_float5>=41 and percentage_float5<=50:
                g = "F"
                r = "PASS"
            else:
                g = "F"
                r = "FAIL"
            
            grade5, result5 = st.columns([1,1])
            with grade5:
                grade5 = st.text_input("Grade", g)
                grade_str5 = str(grade5)
            with result5:
                result5 = st.text_input("Result", r)
                result_str5 = str(result5)
                
    update_result = st.button("Update Result", type="primary")
    
    if update_result:
        
        condition = df['SrNo'] == sr_no_int5
        
        result_data = {
                "SrNo": sr_no_int5,
                "RollNo": roll_no_int5,
                "Name": name_str5,
                "Email": email_str5,
                "English": english_int5,
                "Hindi": hindi_int5, 
                "Maths": maths_int5,
                "SS": ss_int5,
                "Science": science_int5,
                "Total": total_int5,
                "Percentage": percentage_float5,
                "Grade": grade_str5,
                "Result": result_str5,
            }
        
        df.loc[condition, list(result_data.keys())] = list(result_data.values())
        conn.update(worksheet="Sheet1", data=df)
        
        st.success("Result Successfully Updated")