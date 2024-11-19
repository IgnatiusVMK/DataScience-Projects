import pandas as pd
import numpy as np
import streamlit as st
import os

import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

train_data = pd.read_csv('/home/ignatiusvmk/Downloads/home-credit-default-risk/application_train.csv')

def render_model():
    st.title("Model Pipeline")
    st.write("""
            * Aiming to use the model saved via the save_model() function\n
            > `save_model(best_model, 'credit_default_pipeline')`
            """)
    st.image(os.path.join(os.getcwd(), 'static', 'best_model.png'), caption="Model Pipeline")
    
    # Load the data
    df = pd.read_csv('/home/ignatiusvmk/Downloads/home-credit-default-risk/application_train.csv')

    # Clean data: Replace NaNs and infinities
    if df.isnull().sum().any() or np.isinf(df).sum().any():
        st.warning("Data contains NaN or infinite values. Cleaning data...")
        df.fillna(0, inplace=True)  # Fill NaN values
        df.replace([np.inf, -np.inf], 0, inplace=True)  # Replace infinite values

    # Convert Int64 (nullable integer) columns to int
    for col in df.columns:
        if pd.api.types.is_integer_dtype(df[col]):
            df[col] = df[col].astype('int64')

    # Convert non-numeric object columns to category
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].astype('category')

    # Display data types for verification
    st.write("Data types after conversion:")
    st.write(df.dtypes)

    # Debug: Identify columns causing issues
    problematic_cols = []
    for col in df.columns:
        try:
            # Check if the column can be summarized in profiling
            _ = df[col].describe()
        except Exception as e:
            st.write(f"Column '{col}' caused an issue: {e}")
            problematic_cols.append(col)

    # Drop problematic columns (if any)
    if problematic_cols:
        st.write(f"Dropping problematic columns: {problematic_cols}")
        df.drop(columns=problematic_cols, inplace=True)

    # Generate profile report
    try:
        pr = df.profile_report()
        st_profile_report(pr)
    except Exception as e:
        st.error(f"An error occurred while generating the profile report: {e}")