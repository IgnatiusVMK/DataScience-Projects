# # Main app layout and navigation
# def main():
#     if st.session_state.logged_in:
#         # Sidebar Navigation
#         page = st.sidebar.selectbox("Navigation", ["Dashboard", "Datasets","Active Users", "Logout"])
        
#         if page == "Dashboard":
#             render_dashboard()
#         elif page == "Datasets":
#             render_datasets()
#         elif page == "Active Users":
#             render_active_users()
#         elif page == "Logout":
#             logout()
#     else:
#         login()
#         st.subheader("Register a new account")
#         reg_username = st.text_input("New Username", "")
#         reg_password = st.text_input("New Password", type="password")
#         if st.button("Register"):
#             register(reg_username, reg_password)

# # Run the main app
# if __name__ == "__main__":
#     main()


    # def fetch_all_users():
    #     conn = create_connection()
    #     cursor = conn.cursor()

    #     try:
    #         users_query = " SELECT * FROM users"
    #         cursor.execute(users_query)
    #         rows = cursor.fetchall()
    #         columns = [col[0] for col in  cursor.description]
    #     except Error as f:
    #         st.error(f"Error: {f}")
    #         return None

    #     all_users = pd.DataFrame(rows, columns=columns)

    #     cursor.close()
    #     conn.close()

    #     return all_users

    # users =  fetch_all_users()

    # # Display the DataFrame in Streamlit
    # if users is not None:
    #     st.write(users)
    # else:
    #     st.write("No users found or an error occurred.")