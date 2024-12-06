# import pandas as pd
# import numpy as np
# import streamlit as st
# import os
# from pycaret.classification import load_model as pycaret_load_model

# def render_model():
#     st.title("Credit Default Prediction Model")
#     st.write(
#         """
#         This application uses a trained model to predict the likelihood of loan default based on applicant data.
#         The model was saved using the `save_model()` function in PyCaret:
#         ```python
#         save_model(best_model, 'credit_default_pipeline')
#         ```
#         """
#     )
#     st.image(
#         os.path.join(os.getcwd(), 'static', 'best_model.png'), caption="Model Pipeline"
#     )

#     # Load the saved PyCaret model
#     @st.cache_resource
#     def load_saved_model():
#         model_path = os.path.join(
#             '/home', 'ignatiusvmk', 'PycharmProjects', 'DataScience Projects', 
#             'Home Credit Default Risk', 'UnderSample', 'credit_default_pipeline'
#         )
#         return pycaret_load_model(model_path)

#     model = load_saved_model()

#     # Retrieve the model's expected feature columns
#     expected_columns = model.feature_names_in_

#     # Debugging: Display expected features
#     st.write("Model expected columns:", expected_columns)

#     # Input fields for user-provided data (Top 10 important features)
#     user_inputs = {
#         "CREDIT_DURATION_MEAN": st.number_input("CREDIT_DURATION_MEAN", min_value=0.0, step=0.01),
#         "CREDIT_SUM_TOTAL": st.number_input("CREDIT_SUM_TOTAL", min_value=0.0, step=0.01),
#         "AMT_CREDIT": st.number_input("AMT_CREDIT", min_value=0.0, step=0.01),
#         "AMT_GOODS_PRICE": st.number_input("AMT_GOODS_PRICE", min_value=0.0, step=0.01),
#         "DAYS_BIRTH": st.number_input("DAYS_BIRTH", min_value=-100000, step=1),
#         "DAYS_LAST_PHONE_CHANGE": st.number_input("DAYS_LAST_PHONE_CHANGE", min_value=-100000, step=1),
#         "AMT_ANNUITY": st.number_input("AMT_ANNUITY", min_value=0.0, step=0.01),
#         "DAYS_EMPLOYED": st.number_input("DAYS_EMPLOYED", min_value=-100000, step=1),
#         "DAYS_ID_PUBLISH": st.number_input("DAYS_ID_PUBLISH", min_value=-100000, step=1),
#         "PAYMENT_TOTAL": st.number_input("PAYMENT_TOTAL", min_value=0.0, step=0.01),
#     }

#     # Prepare input DataFrame
#     input_data_df = pd.DataFrame([user_inputs])

#     # Ensure all expected columns are present and in correct order
#     for col in expected_columns:
#         if col not in input_data_df.columns:
#             input_data_df[col] = 0  # Add missing columns with default value of 0

#     # Reorder DataFrame to match expected column order
#     input_data_df = input_data_df[expected_columns]

#     # Validate and display the input data
#     st.write("Input data for prediction:")
#     st.write(input_data_df)

#     # Make prediction on button click
#     if st.button("Submit"):
#         try:
#             prediction = model.predict(input_data_df)
#             prediction_label = "High risk of default" if prediction[0] == 1 else "Low risk of default"
#             st.success(f"Prediction: {prediction_label}")
#         except Exception as e:
#             st.error(f"Prediction failed: {e}")

# # Run the application
# if __name__ == "__main__":
#     render_model()

import pandas as pd
import numpy as np
import streamlit as st
import os
from pycaret.classification import load_model as pycaret_load_model

def render_model():
    st.title("Credit Default Prediction Model")
    st.write(
        """
        This application uses a trained model to predict the likelihood of loan default based on applicant data.
        The model was saved using the `save_model()` function in PyCaret:
        ```python
        save_model(best_model, 'credit_default_pipeline')
        ```
        """
    )
    st.image(
        os.path.join(os.getcwd(), 'static', 'best_model.png'), caption="Model Pipeline"
    )

    # Load the saved PyCaret model
    @st.cache_resource
    def load_saved_model():
        model_path = os.path.join(
            '/home', 'ignatiusvmk', 'PycharmProjects', 'DataScience Projects', 
            'Home Credit Default Risk', 'UnderSample', 'credit_default_pipeline'
        )
        return pycaret_load_model(model_path)

    model = load_saved_model()

    # Retrieve the model's expected feature columns
    expected_columns = model.feature_names_in_

    # Debugging: Display expected features
    st.write("Model expected columns:", expected_columns)

    # Input fields for user-provided data (use all expected features)
    user_inputs = {}
    
    for col in expected_columns:
        if col in ["CREDIT_DURATION_MEAN", "CREDIT_SUM_TOTAL", "AMT_CREDIT", 
                    "AMT_GOODS_PRICE", "DAYS_BIRTH", "DAYS_LAST_PHONE_CHANGE", 
                    "AMT_ANNUITY", "DAYS_EMPLOYED", "DAYS_ID_PUBLISH", 
                    "PAYMENT_TOTAL"]:
            user_inputs[col] = st.number_input(col, min_value=0.0, step=0.01)

    # Prepare input DataFrame
    input_data_df = pd.DataFrame([user_inputs])

    # Ensure all expected columns are present and in correct order
    for col in expected_columns:
        if col not in input_data_df.columns:
            input_data_df[col] = 0  # Add missing columns with default value of 0

    # Reorder DataFrame to match expected column order
    input_data_df = input_data_df[expected_columns]

    # Validate and display the input data
    st.write("Input data for prediction:")
    st.write(input_data_df)

    # Make prediction on button click
    if st.button("Submit"):
        try:
            prediction = model.predict(input_data_df)
            prediction_label = "High risk of default" if prediction[0] == 1 else "Low risk of default"
            st.success(f"Prediction: {prediction_label}")
        except Exception as e:
            st.error(f"Prediction failed: {e}")

# Run the application
if __name__ == "__main__":
    render_model()