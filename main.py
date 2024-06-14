# this file added with compatible modules and codes

import streamlit as st
from streamlit_gsheets import GSheetsConnection

# url = "https://docs.google.com/spreadsheets/d/1Lh3WTuBewwYltY4bG0tPq_F095_DNf4eyBdqFlyvYJw/edit?usp=sharing"

st.title("Read and Write Google Sheet using Streamlit GSheetsConnection")
st.subheader("Survey Exercise")
# conn = st.connection("gsheets", type=GSheetsConnection)

# data = conn.read(spreadsheet=url, usecols=[0, 1])
# df = conn.read(worksheet="Sheet1", usecols=[0, 1, 2], ttl=5).dropna(how="all")
# st.dataframe(df, hide_index=True)

# dfEmail = conn.read(worksheet="Sheet1", usecols=[1], ttl=5).dropna(how="all")

# check if emails are unique
# if len(dfEmail) == len(dfEmail.drop_duplicates()):
#     st.write("All emails are unique")
# else:
#     st.write("Duplicate emails found")
col1, col2 = st.columns(2)

with col1:
    if st.button("📑 Take the Survey", use_container_width=True, type="primary"):
        st.switch_page("pages/Survey.py")
with col2:
    if st.button("📊 See Survey Results", use_container_width=True):
        st.switch_page("pages/Result.py")

st.sidebar.markdown("Made with ❤️ by [Mehdi Salari](https://github.com/MehdiSlr) .")