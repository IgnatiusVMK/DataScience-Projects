import pandas as pd
import numpy as np
import streamlit as st
import os
from pycaret.classification import load_model as pycaret_load_model  # Rename PyCaret's load_model

# Load and clean data
train_data = pd.read_csv('/home/ignatiusvmk/Downloads/home-credit-default-risk/application_train.csv')

def render_model():
    st.title("Model Pipeline")
    st.write(
        """
        * Aiming to use the model saved via the `save_model()` function.
        ```
        save_model(best_model, 'credit_default_pipeline')
        ```
        """
    )
    st.image(
        os.path.join(os.getcwd(), 'static', 'best_model.png'), caption="Model Pipeline"
    )

    # Data cleaning: Handle NaN and infinite values
    df = train_data.copy()
    if df.isnull().sum().any() or np.isinf(df).sum().any():
        st.warning("Data contains NaN or infinite values. Cleaning data...")
        df.fillna(0, inplace=True)
        df.replace([np.inf, -np.inf], 0, inplace=True)

    # Convert Int64 columns to int64
    for col in df.columns:
        if pd.api.types.is_integer_dtype(df[col]):
            df[col] = df[col].astype('int64')

    # Convert object columns to category
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype('category')

    # Display cleaned data types
    st.write("Data types after conversion:")
    st.write(df.dtypes)

    # Drop problematic columns (if any)
    problematic_cols = [col for col in df.columns if df[col].dtype not in [np.number, "category"]]
    if problematic_cols:
        st.warning(f"Dropping problematic columns: {problematic_cols}")
        df.drop(columns=problematic_cols, inplace=True)

    # Load the saved PyCaret model
    @st.cache_resource
    def load_saved_model():
        model_path = os.path.join(
            '/home', 'ignatiusvmk', 'PycharmProjects', 'DataScience Projects', 'Home Credit Default Risk', 'UnderSample', 'credit_default_pipeline'
        )
        return pycaret_load_model(model_path)

    model = load_saved_model()

    # Retrieve the model's expected feature columns
    expected_columns = model.feature_names_in_

    # Debugging: Display expected features
    st.write("Model expected columns:", expected_columns)

    # Input fields for user-provided data (Top 10 important features)
    user_inputs = {
        "CREDIT_DURATION_MEAN": st.number_input("CREDIT_DURATION_MEAN", min_value=0.0, step=0.01),
        "CREDIT_SUM_TOTAL": st.number_input("CREDIT_SUM_TOTAL", min_value=0.0, step=0.01),
        "AMT_CREDIT": st.number_input("AMT_CREDIT", min_value=0.0, step=0.01),
        "AMT_GOODS_PRICE": st.number_input("AMT_GOODS_PRICE", min_value=0.0, step=0.01),
        "DAYS_BIRTH": st.number_input("DAYS_BIRTH", min_value=-100000, step=1),
        "DAYS_LAST_PHONE_CHANGE": st.number_input("DAYS_LAST_PHONE_CHANGE", min_value=-100000, step=1),
        "AMT_ANNUITY": st.number_input("AMT_ANNUITY", min_value=0.0, step=0.01),
        "DAYS_EMPLOYED": st.number_input("DAYS_EMPLOYED", min_value=-100000, step=1),
        "DAYS_ID_PUBLISH": st.number_input("DAYS_ID_PUBLISH", min_value=-100000, step=1),
        "PAYMENT_TOTAL": st.number_input("PAYMENT_TOTAL", min_value=0.0, step=0.01),
    }

    # Prepare input DataFrame
    input_data_df = pd.DataFrame([user_inputs])

    # Add missing columns with default values
    for missing_col in set(expected_columns) - set(input_data_df.columns):
        input_data_df[missing_col] = 0

    # Ensure the input DataFrame columns match the expected order
    input_data_df = input_data_df[expected_columns]

    # Validate and display the input data
    st.write("Input data for prediction:")
    st.write(input_data_df)

    # Make prediction
    if st.button("Submit"):
        try:
            prediction = model.predict(input_data_df)
            prediction_label = "High risk of default" if prediction[0] == 1 else "Low risk of default"
            st.success(f"Prediction: {prediction_label}")
        except Exception as e:
            st.error(f"Prediction failed: {e}")



    # @st.cache_resource
    # def load_model(model_path):
    #     # Load the model using PyCaret's load_model function
    #     model = pycaret_load_model(model_path)
        
    #     # Optionally print the type of the model
    #     st.write(f"Loaded model of type: {type(model)}")
        
    #     return model

    # # Define the path to the saved model
    # model_path = os.path.join('/home', 'ignatiusvmk', 'PycharmProjects', 'DataScience Projects', 'Home Credit Default Risk', 'UnderSample', 'credit_default_pipeline')

    # # Load the model
    # model = load_model(model_path)

    # # Streamlit app interface for prediction
    # st.title("Credit Default Prediction")
    # st.write("Input the applicant's information to predict their loan repayment capability.")

    # # Input fields for each feature
    # credit_duration_mean = st.number_input("CREDIT_DURATION_MEAN", min_value=0.0, step=0.01)
    # credit_sum_total = st.number_input("CREDIT_SUM_TOTAL", min_value=0.0, step=0.01)
    # amt_credit = st.number_input("AMT_CREDIT", min_value=0.0, step=0.01)
    # amt_goods_price = st.number_input("AMT_GOODS_PRICE", min_value=0.0, step=0.01)
    # days_birth = st.number_input("DAYS_BIRTH", min_value=-100000, step=1)
    # days_last_phone_change = st.number_input("DAYS_LAST_PHONE_CHANGE", min_value=-100000, step=1)
    # amt_annuity = st.number_input("AMT_ANNUITY", min_value=0.0, step=0.01)
    # days_employed = st.number_input("DAYS_EMPLOYED", min_value=-100000, step=1)
    # days_id_publish = st.number_input("DAYS_ID_PUBLISH", min_value=-100000, step=1)
    # payment_total = st.number_input("PAYMENT_TOTAL", min_value=0.0, step=0.01)

    # input_data_df = pd.DataFrame({
    # "CREDIT_DURATION_MEAN": [credit_duration_mean],
    # "CREDIT_SUM_TOTAL": [credit_sum_total],
    # "AMT_CREDIT": [amt_credit],
    # "AMT_GOODS_PRICE": [amt_goods_price],
    # "DAYS_BIRTH": [days_birth],
    # "DAYS_LAST_PHONE_CHANGE": [days_last_phone_change],
    # "AMT_ANNUITY": [amt_annuity],
    # "DAYS_EMPLOYED": [days_employed],
    # "DAYS_ID_PUBLISH": [days_id_publish],
    # "PAYMENT_TOTAL": [payment_total]
    # })

    # # Make prediction
    # prediction = model.predict(input_data_df)

    # # Display prediction results
    # if prediction[0] == 1:
    #     st.error("High risk of default. Applicant may not be able to repay the loan.")
    # else:
    #     st.success("Low risk of default. Applicant is likely to repay the loan.")