import streamlit as st
from streamlit_gsheets import GSheetsConnection
import altair as alt
import pandas as pd

conn = st.connection("gsheets", type=GSheetsConnection)

col1, col2 = st.columns(2)
with col1:
    st.title("Results")

with col2:
    st.title("")
    if st.button("📑 Take the Survey"):
        st.switch_page("pages/Survey.py")

st.write("### What programming language do you use?")

# Read data from Google Sheets
data = conn.read(worksheet="Sheet1", usecols=[2], ttl=5).dropna(how="all")
data = data['Programming Language'].value_counts().reset_index()
data.columns = ['Programming Language', 'Count']

# Create color scale based on known languages
known_languages = ['Python', 'ASP.NET', 'PHP', 'Dart', 'C++', 'Javascript', 'Go', 'Java', 'Others']
color_scale = alt.Scale(domain=known_languages,
                        range=['#FFDD33', '#9300ff', '#4e5d94', '#00b4ab', '#f34b7e', '#f1e05a', '#00add8', '#af7219', '#B1B1B1'])

# Create bar chart with color scale by Altair
chart = alt.Chart(data).mark_bar().encode(
    x=alt.X('Programming Language:N', sort='-y'),
    y='Count:Q',
    color=alt.condition(
        alt.FieldOneOfPredicate(field='Programming Language', oneOf=known_languages),
        alt.Color('Programming Language:N', scale=color_scale),
        alt.value('#B1B1B1')  # Default color for unknown languages
    )
)

# Display the chart
st.altair_chart(chart, use_container_width=True)

st.sidebar.markdown("Made with ❤️ by [Mehdi Salari](https://github.com/MehdiSlr) .")