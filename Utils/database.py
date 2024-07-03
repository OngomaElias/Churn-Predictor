import streamlit as st
import pyodbc
import pandas as pd

# Create a connection to the database
@st.cache_resource(show_spinner='Connecting to database ...')
def init_connection():
    return pyodbc.connect(
        "DRIVER={SQL Server};SERVER="
        + st.secrets['SERVER_NAME']
        + ";DATABASE="
        + st.secrets['DATABASE_NAME']
        + ";UID="
        + st.secrets['USER']
        + ";PWD="
        + st.secrets['PASSWORD']
    )

# Initialize the connection
connection = init_connection()

@st.cache_data(show_spinner='Running query ...')
def running_query(query):
    with connection.cursor() as c:
        c.execute(query)
        rows = c.fetchall()
        df = pd.DataFrame.from_records(rows, columns=[column[0] for column in c.description])
    return df

def get_all_columns():
    sql_query = "SELECT * FROM " + st.secrets['TABLE_NAME']
    df = running_query(sql_query)
    return df

# Load data once and use it in the session state
if 'dataframe' not in st.session_state:
    st.session_state.dataframe = get_all_columns()
