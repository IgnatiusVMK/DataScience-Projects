import mysql.connector
from mysql.connector import Error
import streamlit as st

from views.dashboard import render_dashboard
from views.docs import render_datasets
from views.users import render_active_users
from views.model import render_model

# Import the connection variables
from db_config import db_config, config2

config = db_config
db_config2 = config2

# Define connection parameters

db_config2= {
    'user': 'credadminvmk',
    'password': 'Vcred@Pass4321',
    'host':'localhost',
    'port': 3306,
    'database': 'cred_default_app',
    'raise_on_warnings': True
}

# Ensure session state is initialized
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "current_page" not in st.session_state:
    st.session_state.current_page = "Login" 

# Database connection function
def create_connection():
    try:
        connection = mysql.connector.connect(**config)
        return connection
    except Error as e:
        st.error(f"Error: {e}")
        return None
    
def create_connection2():
    try:
        connection = mysql.connector.connect(**db_config2)
        return connection
    except Error as e:
        st.error(f"Error: {e}")
        return None

if create_connection is None:
    st.info("Trying to connect with the second configuration...")
    connection = create_connection(db_config2)
# Registration function
def register(username, password):
    if not username:
        st.error("Username cannot be empty.")
        return
    elif not password:
        st.error("Password cannot be empty.")
        return
    
    connection = create_connection2()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            connection.commit()
            st.success("Registration successful! Please log in.")

            # Clear the session state for username and password
            st.session_state['username'] = ""
            st.session_state['password'] = ""
        except mysql.connector.Error as e:
            st.error(f"Registration failed: {e}")
        finally:
            cursor.close()
            connection.close()

# Check login function
def check_login(username, password):
    connection = create_connection2()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        return result is not None
    return False

# @st.cache_data
# Login/Register function
def login(option):
    if option == "Log In":
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Log in"):
            if not username or not password:
                st.error("Username and password cannot be empty.")
            elif check_login(username, password):
                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.current_page = "Dashboard"  # Set Dashboard as default after login
                st.success("Logged in successfully!")
                st.rerun()
            else:
                st.error("Invalid username or password.")

    elif option == "Register":
        username = st.text_input("New Username")
        password = st.text_input("New Password", type="password")
        
        if st.button("Register"):
            if not username:
                st.error("Username cannot be empty.")
            elif not password:
                st.error("Password cannot be empty.")
            else:
                register(username, password)

# Logout function
def logout():
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.session_state.current_page = "Login"
    st.success("Logged out successfully!")
    st.rerun()

# Page Router
def render_page():
    if st.session_state.current_page == "Dashboard":
        render_dashboard()
    elif st.session_state.current_page == "Dataset Docs":
        render_datasets()
    elif st.session_state.current_page == "Active Users":
        render_active_users()
    elif st.session_state.current_page == "Model":
        render_model()
    elif st.session_state.current_page == "Logout":
        logout()

# Main app with button-based navigation
def main():
    if st.session_state.logged_in:
        # Display sidebar navigation options
        st.sidebar.markdown("### Navigation")
        if st.sidebar.button("Dashboard"):
            st.session_state.current_page = "Dashboard"
        if st.sidebar.button("Model"):
            st.session_state.current_page = "Model"
        if st.sidebar.button("Dataset Docs"):
            st.session_state.current_page = "Dataset Docs"
        if st.sidebar.button("Active Users"):
            st.session_state.current_page = "Active Users"
    
        if st.sidebar.button("Logout"):
            st.session_state.current_page = "Logout"
    else:
        # Show login form
        st.sidebar.markdown("## Log in or Register", )
        option = st.sidebar.radio("Select an option:", ("Log In", "Register"))
        login(option)
        
    # Render the selected page
    render_page()

# Run the main app
if __name__ == "__main__":
    main()
