

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import plotly.express as px
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

st.set_page_config(
    page_title='Dashboard Page',
    page_icon='📈',
    layout='wide'
)






if st.session_state['authentication_status']:
    #authenticator.logout(location = 'sidebar')
    st.title('Churn Predictor')






    # Load the dataset
    df = pd.read_csv('./Data/full_data.csv')

    # Sidebar filters
    gender_filter = st.sidebar.selectbox('Gender', options=['All', 'Female', 'Male'])
    payment_filter = st.sidebar.selectbox('Payment Method', options=['All'] + df['PaymentMethod'].unique().tolist())
    contract_filter = st.sidebar.selectbox('Contract', options=['All'] + df['Contract'].unique().tolist())

    # Applying filters
    filtered_df = df.copy()
    if gender_filter != 'All':
        filtered_df = filtered_df[filtered_df['gender'] == gender_filter]

    if payment_filter != 'All':
        filtered_df = filtered_df[filtered_df['PaymentMethod'] == payment_filter]

    if contract_filter != 'All':
        filtered_df = filtered_df[filtered_df['Contract'] == contract_filter]

    def eda_dashboard():
        st.markdown('### EDA Dashboard')

        st.markdown('#### Histograms')
        fig1 = px.histogram(filtered_df, x='tenure', title='Tenure Distribution')
        fig2 = px.histogram(filtered_df, x='MonthlyCharges', title='Monthly Charges Distribution')
        st.plotly_chart(fig1)
        st.plotly_chart(fig2)

        st.markdown('#### Correlation Matrix')
        corr_matrix = filtered_df.select_dtypes(include=['float64', 'int64']).corr()
        fig3, ax = plt.subplots()
        sns.heatmap(corr_matrix, annot=True, ax=ax)
        st.pyplot(fig3)

        st.markdown('#### Average Monthly Charges Trend by Tenure')
        avg_monthly_charges_trend = filtered_df.groupby('tenure')['MonthlyCharges'].mean().reset_index()
        fig4 = px.line(avg_monthly_charges_trend, x='tenure', y='MonthlyCharges', title='Average Monthly Charges by Tenure')
        st.plotly_chart(fig4)

        st.markdown('#### Average Yearly Charges Trend by Tenure')
        filtered_df['YearlyCharges'] = filtered_df['MonthlyCharges'] * 12
        avg_yearly_charges_trend = filtered_df.groupby('tenure')['YearlyCharges'].mean().reset_index()
        fig5 = px.line(avg_yearly_charges_trend, x='tenure', y='YearlyCharges', title='Average Yearly Charges by Tenure')
        st.plotly_chart(fig5)

        st.markdown('#### Churn Rate Trend by Tenure')
        churn_rate_trend = filtered_df.groupby('tenure')['Churn'].apply(lambda x: (x == 'Yes').mean()).reset_index()
        fig6 = px.line(churn_rate_trend, x='tenure', y='Churn', title='Churn Rate by Tenure')
        st.plotly_chart(fig6)





        

        # Rest of your KPI dashboard code




    def kpi_dashboard():

        st.markdown('### Key Performance Indicators')

        total_customers = len(filtered_df)
        churned_customers = filtered_df['Churn'].value_counts().get('Yes', 0)
        churn_rate = (churned_customers / total_customers) * 100
        avg_monthly_charge = filtered_df['MonthlyCharges'].mean()
        avg_total_charge = filtered_df['TotalCharges'].mean()
        avg_tenure = filtered_df['tenure'].mean()
        #avg_yearly_charge = filtered_df['YearlyCharges'].mean()  # Access YearlyCharges after computation

        st.markdown(f"""
        <div style="background-color: #CCE5FF; border-radius: 10px; width: 80%; margin-top: 20px; padding: 10px;">
            <h3>Total Customers: {total_customers}</h3>
            <h3>Churned Customers: {churned_customers}</h3>
            <h3>Churn Rate: {churn_rate:.2f}%</h3>
            <h3>Average Monthly Charge: ${avg_monthly_charge:.2f}</h3>
            <h3>Average Total Charge: ${avg_total_charge:.2f}</h3>
            <h3>Average Tenure (Months): {avg_tenure:.2f}</h3>
            
        </div>
        """, unsafe_allow_html=True)

        st.markdown('### Additional KPIs')
        
        # Add more KPIs as needed

        st.markdown('#### Distribution of Churn')
        churn_distribution = filtered_df['Churn'].value_counts(normalize=True).reset_index()
        churn_distribution.columns = ['Churn', 'proportion']
        fig7 = px.pie(churn_distribution, names='Churn', values='proportion', title='Distribution of Churn')
        st.plotly_chart(fig7)

        st.markdown('#### Churn by Contract')
        churn_by_contract = filtered_df.groupby('Contract')['Churn'].value_counts(normalize=True).unstack()
        fig8, ax1 = plt.subplots()
        churn_by_contract.plot(kind='bar', stacked=True, ax=ax1)
        st.pyplot(fig8)

        st.markdown('#### Churn by Payment Method')
        churn_by_payment = filtered_df.groupby('PaymentMethod')['Churn'].value_counts(normalize=True).unstack()
        fig9, ax2 = plt.subplots()
        churn_by_payment.plot(kind='bar', stacked=True, ax=ax2)
        st.pyplot(fig9)

        st.markdown('#### Churn by Demographics')
        fig10 = px.histogram(filtered_df, x='Churn', color='gender', title='Churn by Gender')
        st.plotly_chart(fig10)

        fig11 = px.histogram(filtered_df, x='Churn', color='Partner', title='Churn by Partner')
        st.plotly_chart(fig11)

        fig12 = px.histogram(filtered_df, x='Churn', color='Dependents', title='Churn by Dependents')
        st.plotly_chart(fig12)

        fig13 = px.histogram(filtered_df, x='Churn', color='SeniorCitizen', title='Churn by Senior Citizen')
        st.plotly_chart(fig13)

        st.markdown('#### Online Backup vs Internet Service')
        fig14 = px.histogram(filtered_df, x='OnlineBackup', color='InternetService', barmode='group', title='Online Backup vs Internet Service')
        st.plotly_chart(fig14)

        st.markdown('#### Phone Service/Multiple Lines vs Churn')
        fig15 = px.histogram(filtered_df, x='PhoneService', color='Churn', barmode='group', title='Phone Service vs Churn')
        st.plotly_chart(fig15)

        fig16 = px.histogram(filtered_df, x='MultipleLines', color='Churn', barmode='group', title='Multiple Lines vs Churn')
        st.plotly_chart(fig16)

        st.markdown('#### Streaming Services vs Churn')
        fig17 = px.histogram(filtered_df, x='StreamingMovies', color='Churn', barmode='group', title='Streaming Movies vs Churn')
        st.plotly_chart(fig17)

        fig18 = px.histogram(filtered_df, x='StreamingTV', color='Churn', barmode='group', title='Streaming TV vs Churn')
        st.plotly_chart(fig18)

        st.markdown('#### Online Security vs Internet Service')
        fig19 = px.histogram(filtered_df, x='OnlineSecurity', color='InternetService', barmode='group', title='Online Security vs Internet Service')
        st.plotly_chart(fig19)

        st.markdown('#### Churn by Paperless Billing')
        fig20 = px.histogram(filtered_df, x='PaperlessBilling', color='Churn', barmode='group', title='Churn by Paperless Billing')
        st.plotly_chart(fig20)

    def main():
        st.title("Customer Churn Dashboard")

        # Sidebar for selecting dashboard type
        dashboard_type = st.sidebar.selectbox('Select Dashboard Type', options=['EDA', 'KPI'])

        if dashboard_type == 'EDA':
            eda_dashboard()
        else:
            kpi_dashboard()

    if __name__ == '__main__':
        main()








elif st.session_state['authentication_status'] is False:
    st.error('Wrong username/password')
elif st.session_state['authentication_status'] is None:
    st.info('Login from the home page to access the app')
    st.code("""
        Test Account
        Username: OngomaElias
        Password: 123456
    """)



#st.write(st.session_state)

