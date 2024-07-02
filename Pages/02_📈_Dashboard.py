

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import plotly.express as px

st.set_page_config(
    page_title='Dashboard Page',
    page_icon='📈',
    layout='wide'
)



df = pd.read_csv('./Data/full_data.csv')

def eda_dashboard():
    st.markdown('### EDA Dashboard')
    col1, col2 = st.columns(2)

    with col1:
        scatter_plot = px.scatter(df, x = 'gender', y ='tenure', title ='gender to tenure distribution',
        color = 'Churn', color_discrete_map = {'Yes':'red','No':'yellow'})

        st.plotly_chart(scatter_plot)
    with col2:
        pass


    gender_histogram = px.histogram(df, x = 'gender')

    st.plotly_chart(gender_histogram)


def kpi_dashboard():
    """
    This function creates a KPI dashboard.
    """
    st.markdown('### Key Performance Indicators')
    
    churn_rate = df['Churn'].value_counts(normalize=True).get('Yes', 0) * 100
    avg_tenure = df['tenure'].mean()
    data_size = df.size

    col1, col2 =st.columns(2)
    with col1:
    
        st.markdown(f"""
        <div style="background-color: #CCE5FF; border-radius: 10px; width: 80%; margin-top: 20px; padding: 10px;">
            <h3 style="margin-left: 10px;">Quick Stats About Dataset</h3>
            <hr>
            <h5 style="margin-left: 10px;">Churn Rate: {churn_rate:.2f}%</h5>
            <hr>
            <h5 style="margin-left: 10px;">Average Tenure: ${avg_tenure:.2f}</h5>
            <hr>
            <h5 style="margin-left: 10px;">Data Size: {data_size}</h5>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        pass










if __name__ == '__main__':
    """
    This block of code is executed when the script is run directly.
    """
    st.title("Dashboard")
    col1, col2 = st.columns(2)
    with col1:
        pass
    with col2:
        selected_dashboard_type = st.selectbox('Select the type of Dashboard', options=['EDA', 'KPI'], key='selected_dashboard_type')
        
    if st.session_state['selected_dashboard_type'] == 'EDA':
        eda_dashboard()
    else:
        kpi_dashboard()



