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
