# users.py

import pandas as pd
import streamlit as st
import mysql.connector
from mysql.connector import Error

def render_active_users():
    
    # Import the connection variables
    from db_config import db_config

    config = db_config
    
    config2 = {
        'user': 'credadminvmk',
        'password': 'Vcred@Pass4321',
        'host':'localhost',
        'port': 3306,
        'database': 'cred_default_app',
        'raise_on_warnings': True
    }

    st.title("Active")

    def create_connection():
        try:
            connection = mysql.connector.connect(**config)
            st.success("Connected to the database.")
            return connection
        except Error as e:
            st.error(f"Database connection failed: {e}")
            return None
    def create_connection2():
        try:
            connection = mysql.connector.connect(**config2)
            st.success("Connected to the database.")
            return connection
        except Error as e:
            st.error(f"Database connection failed: {e}")
            return None

    # @st.cache_data
    def fetch_all_users():
        conn = create_connection()
        users_query = " SELECT * FROM users"
        return pd.read_sql_query(users_query, conn)

    fetch_users = fetch_all_users()

    # Display the DataFrame in Streamlit
    if fetch_users is not None:
        st.write(fetch_users)
    else:
        st.write("No users found or an error occurred.")
    