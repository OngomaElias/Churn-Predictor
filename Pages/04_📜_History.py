import streamlit as st
import pandas as pd
import os

st.set_page_config(
    page_title='Prediction History',
    page_icon='📜',
    layout='wide'
)

st.title('Prediction History 📜')

def load_history():
    file_path = './data/history.csv'
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        return df
    else:
        return pd.DataFrame(columns=['gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure', 'PhoneService',
                                     'MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup',
                                     'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies',
                                     'Contract', 'PaperlessBilling', 'PaymentMethod', 'MonthlyCharges', 
                                     'TotalCharges', 'PredictionTime', 'ModelUsed'])

history_df = load_history()

if history_df.empty:
    st.write("No prediction history available.")
else:
    st.dataframe(history_df)

st.markdown("### Download History")
st.download_button(
    label="Download history as CSV",
    data=history_df.to_csv(index=False).encode('utf-8'),
    file_name='prediction_history.csv',
    mime='text/csv',
)


