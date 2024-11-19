# dashboard.py
import streamlit as st
import pandas as pd
import os

# Render Dashboard Page
def render_dashboard():
    st.title("Home Credit Default Risk")
    st.write("Can you predict how capable each applicant is of repaying a loan?")
    st.divider()
    @st.cache_data
    def load_train_data():
        return pd.read_csv('/home/ignatiusvmk/Downloads/home-credit-default-risk/application_train.csv')
    
    train_df = load_train_data()

    @st.cache_data
    def load_columns_description():
        return pd.read_csv('/home/ignatiusvmk/Downloads/home-credit-default-risk/HomeCredit_columns_description.csv', encoding='utf-8')
    
    columns_description_df = load_columns_description()

    st.write("""
    ## Description
    * Many people struggle to get loans due to insufficient or non-existent credit histories. And, unfortunately, this population is often taken advantage of by untrustworthy lenders.

    ### Home Credit Group

    * Home Credit strives to broaden financial inclusion for the unbanked population by providing a positive and safe borrowing experience. In order to make sure this underserved population has a positive loan experience, Home Credit makes use of a variety of alternative data--including telco and transactional information--to predict their clients' repayment abilities.

    * While Home Credit is currently using various statistical and machine learning methods to make these predictions, they're challenging Kagglers to help them unlock the full potential of their data. Doing so will ensure that clients capable of repayment are not rejected and that loans are given with a principal, maturity, and repayment calendar that will empower their clients to be successful.     
    """)

    st.divider()

    st.write("""
    ### HomeCredit_columns_description.csv
    * This file contains descriptions for the columns in the various data files.
    """
    )
    st.dataframe(columns_description_df)
    st.divider()

    st.write("""
    ### application_{train|test}.csv

    * This is the main table, broken into two files for Train (with TARGET) and Test (without TARGET).
    * Static data for all applications. One row represents one loan in our data sample.
    """)
    st.dataframe(train_df)
    st.divider()

    st.image(os.path.join(os.getcwd(), 'static', 'home_credit.png'), caption="Datasets Relation")