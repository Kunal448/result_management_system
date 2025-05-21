import streamlit as st
from fpdf import FPDF
import time
import os
import smtplib
import pandas as pd
from email.message import EmailMessage
from streamlit_gsheets import GSheetsConnection

def page7():
    st.title("Send Results")
    url = "https://docs.google.com/spreadsheets/d/1Bd7iDW_uNA-ttIMYgtsFBs7fFlx-Yzq9DEMCdPNKFxg/edit?usp=sharing"

    conn = st.connection("gsheets", type = GSheetsConnection)
    
    data = conn.read(worksheet="Sheet1", ttl=3)
    df = pd.DataFrame(data)
    
    if st.button("Send Results", type='primary'):
        maximum = df['SrNo'].max()
    
        #for i in range(1, (int(maximum)+1), 1):
            
            
        for index, row in df.iterrows():
            try:
                os.remove("Result.pdf")
            except:
                pass                
            pdf = FPDF()
            pdf.add_page()
            
            pdf.set_font("Times", size = 22, style = 'B')
            pdf.cell(200, 10, txt = "Class 10 CBSE Board Results", ln = 1, align = 'C')
            
            pdf.set_font("Times", size = 22, style = 'B')
            pdf.cell(200, 10, txt = "Term 2022-23", align = 'C')
            
            pdf.set_xy(5, 28)
            
            pdf.set_font("Arial", size = 16)
            pdf.cell(200, 10, txt = "-"*105, align = 'L')
            
            #new
            pdf.set_xy(10, 35)
            
            pdf.set_font("Arial", size = 16, style = 'B')
            pdf.cell(200, 10, txt = "Name:-", align = 'L')
            
            pdf.set_xy(31, 35)
            
            pdf.set_font("Arial", size = 16)
            pdf.cell(200, 10, txt = str(row['Name']), align = 'L')
            
            pdf.set_xy(10, 43)
            
            pdf.set_font("Arial", size = 16, style = 'B')
            pdf.cell(200, 10, txt = "Class:-", align = 'L')
            
            pdf.set_xy(30, 43)
            
            pdf.set_font("Arial", size = 16)
            pdf.cell(200, 10, txt = "10", align = 'L')
        
            pdf.set_xy(10, 51)
            
            pdf.set_font("Arial", size = 16, style = 'B')
            pdf.cell(200, 10, txt = "Roll No:-", align = 'L')
            
            pdf.set_xy(35, 51)
            
            pdf.set_font("Arial", size = 16)
            pdf.cell(200, 10, txt = str(row['RollNo']), align = 'L')
            
            pdf.set_xy(5, 58)
            
            pdf.set_font("Arial", size = 16)
            pdf.cell(200, 10, txt = "-"*105, align = 'L')
            
            pdf.set_xy(15, 65)
            
            pdf.set_font("Arial", size = 18, style = 'B')
            pdf.cell(200, 10, txt = "Subject", align = 'L')
        
            pdf.set_xy(80, 65)
            
            pdf.set_font("Arial", size = 18, style = 'B')
            pdf.cell(200, 10, txt = "Marks", align = 'L')
            
            pdf.set_xy(17, 73)
            
            pdf.set_font("Arial", size = 16)
            pdf.cell(200, 10, txt = "English", align = 'L')
            
            pdf.set_xy(85, 73)
            
            pdf.set_font("Arial", size = 16)
            pdf.cell(200, 10, txt = str(row['English']), align = 'L')
            
            pdf.set_xy(19, 80)
            
            pdf.set_font("Arial", size = 16)
            pdf.cell(200, 10, txt = "Hindi", align = 'L')
        
            pdf.set_xy(85, 80)
            
            pdf.set_font("Arial", size = 16)
            pdf.cell(200, 10, txt = str(row['Hindi']), align = 'L')
            
            pdf.set_xy(18, 87)
            
            pdf.set_font("Arial", size = 16)
            pdf.cell(200, 10, txt = "Maths", align = 'L')
            
            pdf.set_xy(85, 87)
            
            pdf.set_font("Arial", size = 16)
            pdf.cell(200, 10, txt = str(row['Maths']), align = 'L')
            
            pdf.set_xy(10, 94)
        
            pdf.set_font("Arial", size = 16)
            pdf.cell(200, 10, txt = "Social Science", align = 'L')
            
            pdf.set_xy(85, 94)
            
            pdf.set_font("Arial", size = 16)
            pdf.cell(200, 10, txt = str(row['SS']), align = 'L')
            
            pdf.set_xy(17, 101)
            
            pdf.set_font("Arial", size = 16)
            pdf.cell(200, 10, txt = "Science", align = 'L')
            
            pdf.set_xy(85, 101)
            
            pdf.set_font("Arial", size = 16)
            pdf.cell(200, 10, txt = str(row['Science']), align = 'L')
            
            pdf.set_xy(5, 107)
        
            pdf.set_font("Arial", size = 16)
            pdf.cell(200, 10, txt = "-"*105, align = 'L')
            
            pdf.set_xy(10, 114)
            
            pdf.set_font("Arial", size = 16, style = 'B')
            pdf.cell(200, 10, txt = "Total Marks:-", align = 'L')
            
            pdf.set_xy(47, 114)
            
            pdf.set_font("Arial", size = 16)
            pdf.cell(200, 10, txt = str(row['Total']), align = 'L')
            
            pdf.set_xy(10, 121)
            
            pdf.set_font("Arial", size = 16, style = 'B')
            pdf.cell(200, 10, txt = "Percentage:-", align = 'L')
            
            pdf.set_xy(46, 121)
        
            pdf.set_font("Arial", size = 16)
            pdf.cell(200, 10, txt = "{}%".format(str(row['Percentage'])), align = 'L')
            
            pdf.set_xy(5, 127)
            
            pdf.set_font("Arial", size = 16)
            pdf.cell(200, 10, txt = "-"*105, align = 'L')
            
            pdf.set_xy(10, 134)
            
            pdf.set_font("Arial", size = 16, style = 'B')
            pdf.cell(200, 10, txt = "Grade:-", align = 'L')
            
            pdf.set_xy(32, 134)
            
            pdf.set_font("Arial", size = 16)
            pdf.cell(200, 10, txt = str(row['Grade']), align = 'L')
            
            pdf.set_xy(120, 134)
        
            pdf.set_font("Arial", size = 16, style = 'B')
            pdf.cell(200, 10, txt = "Result:-", align = 'L')
            
            pdf.set_xy(143, 134)
            
            pdf.set_font("Arial", size = 16)
            pdf.cell(200, 10, txt = str(row['Result']), align = 'L')
            
            pdf.output("Result.pdf")
        
            add = "powerhousekunal@gmail.com"
            psd = "xuri dfvo ggho qkeg"
            
            content = f'''Hello Student!
            This is to inform you that result of CBSE Board class 10 has been announced.
            Kindly check the below attachment to see your result.
            
            All the best for your future.'''
            
            msg = EmailMessage()
            msg['Subject'] = "Class 10 Result of {}".format(str(row['Name']))
            msg['From'] = add
            msg['To'] = "{}".format(str(row['Email']))
            msg.set_content(content)
            
            files = ["Result.pdf"]
        
            for file in files:
                with open(file, 'rb') as f:
                    file_data = f.read()
                    file_name = f.name
            
                msg.add_attachment(file_data, maintype = "application", subtype = "octet-stream", filename = file_name)
            
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(add, psd)
                smtp.send_message(msg)
        time.sleep(3)
        st.success("Results Sent Successfully!")