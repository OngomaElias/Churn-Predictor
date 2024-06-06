# utils.py
import pandas as pd

def preprocess_input(input_data):
    # Example preprocessing steps
    df = pd.DataFrame([input_data])
    df.fillna(0, inplace=True)
    # Add more preprocessing steps as needed
    return df





def preprocess_input(input_data):
    input_data['gender'] = input_data['gender'].map({'Male': 0, 'Female': 1})
    input_data['MultipleLines'] = input_data['MultipleLines'].map({'No phone service': 0, 'No': 1, 'Yes': 2})
    input_data['InternetService'] = input_data['InternetService'].map({'No': 0, 'DSL': 1, 'Fiber optic': 2})
    input_data['OnlineSecurity'] = input_data['OnlineSecurity'].map({'No internet service': 0, 'No': 1, 'Yes': 2})
    input_data['DeviceProtection'] = input_data['DeviceProtection'].map({'No internet service': 0, 'No': 1, 'Yes': 2})
    input_data['TechSupport'] = input_data['TechSupport'].map({'No internet service': 0, 'No': 1, 'Yes': 2})
    input_data['StreamingTV'] = input_data['StreamingTV'].map({'No internet service': 0, 'No': 1, 'Yes': 2})
    input_data['StreamingMovies'] = input_data['StreamingMovies'].map({'No internet service': 0, 'No': 1, 'Yes': 2})
    input_data['Contract'] = input_data['Contract'].map({'Month-to-month': 0, 'One year': 1, 'Two year': 2})
    input_data['PaperlessBilling'] = input_data['PaperlessBilling'].astype(int)
    input_data['PaymentMethod'] = input_data['PaymentMethod'].map({
        'Electronic check': 0,
        'Mailed check': 1,
        'Bank transfer (automatic)': 2,
        'Credit card (automatic)': 3
    })
    input_data['TotalCharges'] = pd.to_numeric(input_data['TotalCharges'], errors='coerce')
    input_data = input_data.fillna(0)  # Fill NaN values with 0
    return input_data
