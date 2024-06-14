import streamlit as st
from streamlit_gsheets import GSheetsConnection
import pandas as pd

conn = st.connection("gsheets", type=GSheetsConnection)

st.title("Survey")

st.write("### What programming language do you use?")

# Main inputs
name = st.text_input(label="Name",autocomplete="off")
if name == "":
    st.caption(":red[Name is required.]")
email = st.text_input(label="Email")
if email == "":
    st.caption(":red[Email is required.]")
pl = st.selectbox(label="Programming Language", options=["Select a programming language", "Python", "ASP.NET", "PHP", "Dart", "C++", "Javascript", "Go", "Java", "Other..."])
if pl == "Select a programming language":
    st.caption(":red[Programming language is required.]")

# Dynamic storage for additional input
other_pl = None
if pl == "Other...":
    other_pl = st.text_input(label="Please specify your programming language:")

col1, col2 = st.columns(2)

with col1:
# Submit button
    submit = st.button(label="📑 Submit", type="primary", use_container_width=True)

# Check inputs and display error message if any field is empty
if submit:
    if not name:
        nameEroor = st.error("Name is required.")
    if not email:
        st.error("Email is required.")
    if pl == "Select a programming language":
        st.error("Programming language is required.")
    if pl == "Other..." and not other_pl:
        st.error("Please specify your programming language.")
    
    # If all inputs are filled, display the information
    if name and email and pl != "Select a programming language" and (pl != "Other..." or other_pl):
        if pl == "Other...":
            pl = other_pl
        
        # Read data from Google Sheets and add a new row
        df = conn.read(worksheet="Sheet1", usecols=[0, 1, 2]).dropna(how="all")
        df_email = df['Email'].tolist()

        # Check if email already exists
        if email in df_email:
            st.error("Email already exists in the survey.")
        else:
            data = {'Name': name, 'Email': email, 'Programming Language': pl}
            
            temp_df = pd.DataFrame([data])
            updated_df = pd.concat([df, temp_df])
            conn.update(data=updated_df)
            
            # Display the information
            st.success("Thank you for taking the survey!")
            st.write(f"Name: {name}")
            st.write(f"Email: {email}")
            st.write(f"Selected Programming Language: {pl}")

with col2:
    # Button to go to survey results page
    if st.button("📊 See Results", use_container_width=True):
        st.switch_page("pages/Result.py")

st.sidebar.markdown("Made with ❤️ by [Mehdi Salari](https://github.com/MehdiSlr) .")