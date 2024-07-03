import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

st.set_page_config(
    page_title='Home Page',
    page_icon='🏠',
    layout='wide'
)



with open('./config.yaml') as file:
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['pre-authorized']
)

name, authentication_status, username = authenticator.login(location='sidebar')

if st.session_state['authentication_status']:
    authenticator.logout(location = 'sidebar')
    st.title('Churn Predictor')

    


    # Sample text for the sections
    home_text = "Welcome to the Churn Predictor application. Here, you can analyze customer churn data and gain valuable insights into retention strategies."

    # How to run the application text
    how_to_run_text = "To run the application, simply navigate through the sidebar and select the page you need to view. Follow the instructions on each page."

    key_features_text = """
    - **View Data:** Access the Telcho Churn Database 
    - **Dashboard:** Explore visuals for insights.
    - **Prediction:** See real-time predictions for customers
    - **History:** View past predictions made
    """

    user_benefits_text = """
    - **Proactive Retention:** Understand customer churn trends
    - **Data-Driven Insights:** Utilize detailed visualizations to inform decisions.
    - **Cost Efficiency:** Lower acquisition costs and boost revenue by retaining customers.
    """

    # Layout with columns
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Customer Churn Insight")
        st.write(home_text)

        # User benefits section
        st.subheader("User Benefits")
        st.write(user_benefits_text)
    

    with col2:
        st.subheader("How to Run Application")
        st.write(how_to_run_text)

        # Key features section
        st.subheader("Key Features")
        st.write(key_features_text)

        # Need help section
        st.subheader("Need Help?")
        st.write("For collaborations, contact me at ongomaelias2@gmail.com")

        # Repository on Github button
        st.markdown(
            """
            <style>
            .button {
                display: inline-block;
                padding: 7px 14px;
                font-size: 14px;
                cursor: pointer;
                text-align: center;
                text-decoration: none;
                outline: none;
                color: #fff;
                background-color: #4CAF50;
                border: none;
                border-radius: 5px;
            }
            .button:hover {background-color: #45a049}
            </style>
            <a href="https://github.com/OngomaElias/Customer_Churn-Prediction" class="button">Repository on Github</a>
            """,
            unsafe_allow_html=True
        )











elif st.session_state['authentication_status'] is False:
    st.error('Wrong username/password')
elif st.session_state['authentication_status'] is None:
    st.info('Login to get access to the app')
    st.code("""
        Test Account
        Username: OngomaElias
        Password: 123456
    """)



#st.write(st.session_state)


