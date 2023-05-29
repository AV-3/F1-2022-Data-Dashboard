import streamlit as st
import pandas as pd

#Sets page layout/allows the columns and graphs to use 100% width of the screen
st.set_page_config(page_title= "Grand Prix Results • F1 Dashboard", layout="wide", page_icon=":checkered_flag:")

#Import CSS
with open("styles.css") as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

#Import csv files
df1 = pd.read_csv("raw_csv/GrandPrix_RaceData.csv")
df2 = pd.read_csv("raw_csv/GrandPrix_Qualifying.csv")
df3 = pd.read_csv("raw_csv/GrandPrix_FastestLaps.csv")
df4 = pd.read_csv("raw_csv/races.csv")
df5 = pd.read_csv("raw_csv/drivers.csv")

#Page title
st.title("F1 2022 Grand Prix Statistics")

#Sidebar functionality
race_select = st.sidebar.selectbox("Grand Prix", df4["Grand Prix"].unique())
st.subheader(f"Grand Prix: {race_select}")

#Tab setup
tab1, tab2, tab3 = st.tabs(["Race Results", "Qualifying", "Fastest Laps"])

#Bahrain Stats
bahrain_df1 = df1.iloc[0:20,:]
bahrain_df2 = df2.iloc[0:20,:]
bahrain_df3 = df3.iloc[0:20,:]

st.image("images/F1 Bahrain.png")

if race_select == "Bahrain":
    with tab1:
        st.subheader("Podium")
        col1, col2, col3 = st.columns(3)
        col1.metric("CHARLES LECLERC (Ferrari)", "1st", "26 pts")
        col2.metric("CARLOS SAINZ (Ferrari)", "2nd", "18 pts")
        col3.metric("LEWIS HAMILTON (Mercedes)", "3rd","15 pts")
        st.table(bahrain_df1)
    with tab2:
        st.table(bahrain_df2)
    with tab3:
        st.table(bahrain_df3)
# # Add a dropdown to select the team
# team_dropdwon = st.sidebar.selectbox("Team", df2["Team"].unique())

# # Add a dropdown to select the driver
# driver_dropdown = st.sidebar.selectbox("Driver", df1["Driver"].unique())


# Show the driver's name and team
# st.write(f"Grand Prix: {grandprix_dropdown}")
# st.write(f"Team: {df1[df1['Driver'] == driver_dropdown]['Driver'].values[0]}")
