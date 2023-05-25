import streamlit as st
import pandas as pd

#Sets page layout/allows the columns and graphs to use 100% width of the screen
st.set_page_config(page_title= "Overall Results • F1 Dashboard", layout="wide")


#Import CSS
with open("styles.css") as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

#Import csv files
df1 = pd.read_csv("csv/drivers.csv")
df2 = pd.read_csv("csv/teams.csv")
df3 = pd.read_csv("csv/races.csv")

#Page title
st.title("F1 2022 Season Overview")

#Sets variables for columns
col1, col2, col3 = st.columns(3)

#Column1
with col1:
    col1.header("Drivers Standings")
    st.dataframe(df1)

#Column2
with col2:
    col2.header("Teams Standings")
    st.dataframe(df2)

#Column3
with col3:
    col3.header("Grand Prix Winners")
    st.dataframe(df3)

st.bar_chart(df2.drop(columns=['Pos'], axis=1))