

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.set_page_config(
    page_title='Dashboard Page',
    page_icon='📈',
    layout='wide'
)

def load_csv(file_path):
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        return df
    else:
        st.error(f"File not found at {file_path}")
        return None

def app():
    st.title("Dashboard")
    st.write("Visualize data and model performance here.")
    
    file_path = "./Data/full_data.csv"
    
    # Load the CSV file
    df = load_csv(file_path)
    
    if df is not None:
        # Check unique values in the 'Churn' column
        unique_churn_values = df['Churn'].unique()
        st.write("Unique Churn Values:", unique_churn_values)
        
        # Convert non-numeric values to NaN
        df['Churn'] = pd.to_numeric(df['Churn'], errors='coerce')
        
        # Drop rows with NaN values in the 'Churn' column
        df.dropna(subset=['Churn'], inplace=True)
        
        st.write("Summary Statistics")
        st.write(df.describe())

        # Univariate Analysis
        st.write("Univariate Analysis")
        for column in df.columns:
            if df[column].dtype in ['float64', 'int64']:  # Numeric columns
                fig, ax = plt.subplots()
                df[column].hist(bins=30, ax=ax)
                ax.set_title(f'{column} Distribution')
                ax.set_xlabel(column)
                ax.set_ylabel('Frequency')
                st.pyplot(fig)
            else:  # Categorical columns
                st.write(df[column].value_counts())

        st.write("Total Churn Rate")
        total_churn_rate = df['Churn'].mean()
        st.write("Total Churn Rate:", total_churn_rate)

        # Rest of the code...
    else:
        st.write("No data to display.")

# Call the app function to run the Streamlit app
app()

