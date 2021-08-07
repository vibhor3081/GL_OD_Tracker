# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import base64
import dateutil
import mysql.connector as sql
import os
import pandas as pd
import streamlit as st
import ruamel.yaml as yaml
import lib
import deetly as dl
import numpy as np
import streamlit.components.v1 as components
import streamlit as st
import streamlit.components.v1 as components
import streamlit as st


st.set_page_config(layout="wide")



_selectable_data_table = components.declare_component(
    "selectable_data_table", url="http://localhost:3000",
)


def selectable_data_table(data, key):
    return _selectable_data_table(data=data, default=[], key=key)

#st_custom_slider()





db_config = dict([
    ('hostname', 'canvasdb.caxvr8jox9y6.us-east-2.rds.amazonaws.com'),
    ('port', 3306),
    ('username', 'admin'),
    ('password', '77YnH0bqO8oHMYZGmu78'),
    ('database', 'Vriddhi')
])


DATA_DIR = 'DataFiles'

GL_STATE_COLUMNS = """GL_IntOD_OB
                    GL_IntOD_CB
                    GL_Overdue_CB
                    GL_Overdue_CB
                    GL_Balance_CB
                    GL_RegCharge
                    GL_TransferIn_CB
                    GL_RegBalance_CB
                    GL_OD_Level
                    GL_IntOD_Level
                 """.split()

GL_Data_Table = 'Curr_Accounts_2021_07_GL'

Account_Details_Table = 'Curr_User_Member'

trans_details = GL_STATE_COLUMNS

conn = sql.connect(host=db_config['hostname'], port=db_config['port'], user=db_config['username'], password=db_config['password'], database=db_config['database'])

Account_Detail = pd.read_sql(f"SELECT MemNum, FieldOfficer, BranchName, Community FROM Curr_User_Member",
                                  conn)

GL_Account_Data = pd.read_sql(f"SELECT * FROM Curr_Accounts_2021_07_GL",
                                  conn)


GL_Account_Final = pd.merge(GL_Account_Data, Account_Detail, on = "MemNum", how = "left")

key = "a"

st.sidebar.selectbox('Select your Branch:', GL_Account_Final.BranchName.unique())

st.sidebar.selectbox('Select your Community:', GL_Account_Final.BranchName.unique())

print(GL_Account_Final.BranchName.unique())

for BranchName in GL_Account_Final.BranchName.unique():

    for community in GL_Account_Final.Community.unique():

            df = GL_Account_Final[(GL_Account_Final.BranchName == BranchName) & (GL_Account_Final.Community == community)]

            df2 = df[['MemNum', 'GL_OD_Change', 'GL_IntOD_Change', 'GL_IntOD_Level','GL_OD_Level','BranchName', 'Community']]

            #df2 = df2.groupby(df2['Community'])

            floats  = [float(x) for x in df2['GL_IntOD_Level']]
            floats2 = [float(x) for x in df2['GL_OD_Level']]

            GL_IntOD_Level_Avg = 1
            GL_OD_Level_Avg = 1
            x = ' '
            key = key + "a"

            if(len(df2['GL_IntOD_Level'])):

                GL_IntOD_Level_Avg = sum(floats)/len(df2['GL_IntOD_Level'])
                GL_OD_Level_Avg = sum(floats2)/len(df2['GL_OD_Level'])
                print(GL_IntOD_Level_Avg)

            with st.beta_expander(f"BranchName: {BranchName}   Interest_OD_Average: {format(GL_IntOD_Level_Avg, '.2f')}    GL_OD_Average: {format(GL_OD_Level_Avg, '.2f')}"):

                selectable_data_table(df2, key = key)





