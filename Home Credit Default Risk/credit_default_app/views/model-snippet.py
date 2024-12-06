@st.cache_resource
def load_saved_model():
    # Define the path to the saved model
    model_path = os.path.join('/home', 'ignatiusvmk', 'PycharmProjects', 'DataScience Projects', 'Home Credit Default Risk', 'UnderSample', 'credit_default_pipeline')
    return pycaret_load_model(model_path)

model = load_saved_model()



""" @st.cache_resource
    def load_cached_model():
        # Define the path to the saved model
        model_path = os.path.join('/home', 'ignatiusvmk', 'PycharmProjects', 'DataScience Projects', 'Home Credit Default Risk', 'UnderSample', 'credit_default_pipeline')
        
        # Load the model using PyCaret's load_model function
        model = pycaret_load_model(model_path)
        
        # Optionally print the type of the model
        st.write(f"Loaded model of type: {type(model)}")
        
        # Access the final estimator from the pipeline
        final_estimator = model._final_estimator
        
        # If the final estimator is a model like GradientBoostingClassifier,
        # you can access its features (e.g., feature_importances_).
        if hasattr(final_estimator, 'feature_importances_'):
            st.write(f"Feature importances: {final_estimator.feature_importances_}")
        
        # Alternatively, if you're looking for the expected feature names
        # (assuming the model was trained with column names):
        try:
            expected_features = model.get_config('X_train').columns
            st.write(f"Expected features: {expected_features}")
        except AttributeError:
            st.write("Could not retrieve expected features.")
        
        return model

    # Load the model
    model = load_cached_model() """



@st.cache_resource
    def load_saved_model():
        # Path to your saved model
        model_path = os.path.join('/home', 'ignatiusvmk', 'PycharmProjects', 'DataScience Projects', 'Home Credit Default Risk', 'UnderSample', 'credit_default_pipeline')
        return pycaret_load_model(model_path)

    model = load_saved_model()

    # Get expected features from the model pipeline
    expected_columns = model.named_steps["preprocessor"].transformers_[0][1].get_feature_names_out()


    # Streamlit app interface for prediction
    st.title("Credit Default Prediction")
    st.write("Input the applicant's information to predict their loan repayment capability.")

    # Input fields for each feature
    credit_duration_mean = st.number_input("CREDIT_DURATION_MEAN", min_value=0.0, step=0.01)
    credit_sum_total = st.number_input("CREDIT_SUM_TOTAL", min_value=0.0, step=0.01)
    amt_credit = st.number_input("AMT_CREDIT", min_value=0.0, step=0.01)
    amt_goods_price = st.number_input("AMT_GOODS_PRICE", min_value=0.0, step=0.01)
    days_birth = st.number_input("DAYS_BIRTH", min_value=-100000, step=1)
    days_last_phone_change = st.number_input("DAYS_LAST_PHONE_CHANGE", min_value=-100000, step=1)
    amt_annuity = st.number_input("AMT_ANNUITY", min_value=0.0, step=0.01)
    days_employed = st.number_input("DAYS_EMPLOYED", min_value=-100000, step=1)
    days_id_publish = st.number_input("DAYS_ID_PUBLISH", min_value=-100000, step=1)
    payment_total = st.number_input("PAYMENT_TOTAL", min_value=0.0, step=0.01)

    # Use training dataset features or PyCaret pipeline's expected columns
    expected_columns = list(train_data.columns)

    # Create DataFrame from user input
    input_data_dict = {
        "CREDIT_DURATION_MEAN": credit_duration_mean,
        "CREDIT_SUM_TOTAL": credit_sum_total,
        "AMT_CREDIT": amt_credit,
        "AMT_GOODS_PRICE": amt_goods_price,
        "DAYS_BIRTH": days_birth,
        "DAYS_LAST_PHONE_CHANGE": days_last_phone_change,
        "AMT_ANNUITY": amt_annuity,
        "DAYS_EMPLOYED": days_employed,
        "DAYS_ID_PUBLISH": days_id_publish,
        "PAYMENT_TOTAL": payment_total,
    }

    input_data_df = pd.DataFrame([input_data_dict])

    # Add missing columns with default values
    for missing_col in set(expected_columns) - set(input_data_df.columns):
        input_data_df[missing_col] = 0  # Default value for missing columns

    # Ensure input data has columns in the expected order
    input_data_df = input_data_df[expected_columns]