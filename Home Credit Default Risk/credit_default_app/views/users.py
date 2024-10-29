# users.py

import pandas as pd
import streamlit as st
import mysql.connector
from mysql.connector import Error

def render_active_users():
    # Import the connection variables
    from db_config import db_config

    config = db_config

    st.title("Active")

    def create_connection():
        try:
            connection = mysql.connector.connect(**config)
            st.success("Connected to the database.")
            return connection
        except Error as e:
            st.error(f"Database connection failed: {e}")
            return None

    def fetch_all_users():
        conn = create_connection()
        cursor = conn.cursor()

        try:
            users_query = " SELECT * FROM users"
            cursor.execute(users_query)
            rows = cursor.fetchall()
            columns = [col[0] for col in  cursor.description]
        except Error as f:
            st.error(f"Error: {f}")
            return None

        all_users = pd.DataFrame(rows, columns=columns)

        cursor.close()
        conn.close()

        return all_users

    users =  fetch_all_users()

    # Display the DataFrame in Streamlit
    if users is not None:
        st.write(users)
    else:
        st.write("No users found or an error occurred.")
