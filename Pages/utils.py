# utils.py
import pandas as pd

import streamlit as st

import pandas as pd

def preprocess_input(input_data):
    # Ensure input_data is a DataFrame
    if isinstance(input_data, dict):
        input_data = pd.DataFrame([input_data])
    
    # Print input_data to debug
    print("Input Data:")
    print(input_data)
    
    # Define all possible categorical values
    categorical_values = {
        'gender': ['Male', 'Female'],
        'SeniorCitizen': [0, 1],
        'Partner': [True, False],
        'Dependents': [True, False],
        'PhoneService': [True, False],
        'MultipleLines': ['Yes', 'No', 'No phone service'],
        'InternetService': ['DSL', 'Fiber optic', 'No'],
        'OnlineSecurity': ['Yes', 'No', 'No internet service'],
        'OnlineBackup': ['Yes', 'No', 'No internet service'],
        'DeviceProtection': ['Yes', 'No', 'No internet service'],
        'TechSupport': ['Yes', 'No', 'No internet service'],
        'StreamingTV': ['Yes', 'No', 'No internet service'],
        'StreamingMovies': ['Yes', 'No', 'No internet service'],
        'Contract': ['Month-to-month', 'One year', 'Two year'],
        'PaperlessBilling': [True, False],
        'PaymentMethod': ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)'],
    }
    
    # Fill missing columns with empty strings
    for col in categorical_values.keys():
        if col not in input_data.columns:
            input_data[col] = ''
    
    # Convert boolean fields
    boolean_fields = ['Partner', 'Dependents', 'PaperlessBilling', 'PhoneService', 'SeniorCitizen']
    for field in boolean_fields:
        if field in input_data.columns:
            input_data[field] = input_data[field].map({True: 1, False: 0})
    
    # Convert categorical fields to string
    for field, values in categorical_values.items():
        if field in input_data.columns:
            input_data[field] = pd.Categorical(input_data[field], categories=values).codes
    
    # Ensure all required columns are present
    required_columns = set(categorical_values.keys()) | {'MonthlyCharges', 'TotalCharges'}
    if not required_columns.issubset(set(input_data.columns)):
        missing_columns = required_columns - set(input_data.columns)
        raise ValueError(f"Missing columns: {missing_columns}")
    
    return input_data
