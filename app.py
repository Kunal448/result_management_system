import streamlit as st
from streamlit_option_menu import option_menu

# Import your pages here
import home, new_result, view_result, analyze_result, update_result, delete_result, send_results

st.set_page_config(
    page_title="Result_Web_App",
    page_icon="📑",
    initial_sidebar_state="expanded"
)
with st.sidebar:
    selected = option_menu(
        "Main Menu", ["Home", "New Result", "View Result", "Analyze Result", "Update Result", "Delete Result", "Send Results"],
        icons=[],
        menu_icon="cast", default_index=0,
        styles={
        }
    )
    
#st.write("[![Home](<https://unsplash.com/photos/logo-z7ICBEMUJfw>)](<https://www.google.com/>)")    

# Page content based on selection
if selected == "Home":
    home.page()
elif selected == "New Result":
    new_result.page2()
elif selected == "View Result":
    view_result.page3()
elif selected == "Analyze Result":
    analyze_result.page4()
elif selected == "Update Result":
    update_result.page5()
elif selected == "Delete Result":
    delete_result.page6()
elif selected == "Send Results":
    send_results.page7()
else:
    st.warning("Select Page Above")
