import streamlit as st
import hashlib

st.set_page_config(
    page_title='Home Page',
    page_icon='🏠',
    layout='wide'
)

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

# Placeholder for storing user data and login history (replace with your actual database or storage mechanism)
user_data = []
login_history = []

# Initialize session state and set logged_in to True by default
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = True  # Set to True by default to allow access
if 'creating_account' not in st.session_state:
    st.session_state.creating_account = False

def login_form():
    """
    Creates a login form with username and password fields.
    """
    st.sidebar.header("Login")
    if not st.session_state.creating_account:
        username = st.sidebar.text_input("Username:", key="login_username")
        password = st.sidebar.text_input("Password:", type="password", key="login_password")  # Password field hides the characters
        login_button = st.sidebar.button("Login")

        if login_button:
            # Add logic to handle login button click based on your authentication method
            if authenticate_user(username, password):
                st.session_state.logged_in = True
                st.sidebar.success("Login successful!")
                login_history.append({"username": username, "status": "Success"})
                st.experimental_rerun()  # Refresh the page to reflect the login status
            else:
                st.sidebar.error("Invalid username or password.")
                login_history.append({"username": username, "status": "Failed"})

        create_account_button = st.sidebar.button("Create new account")

        if create_account_button:
            st.session_state.creating_account = True

    else:
        st.sidebar.subheader("Create New Account")
        new_username = st.sidebar.text_input("Username:", key="new_username")
        new_email = st.sidebar.text_input("Email:", key="new_email")
        new_phone_number = st.sidebar.text_input("Phone Number:", key="new_phone_number")
        new_password = st.sidebar.text_input("Password:", type="password", key="new_password")
        confirm_password = st.sidebar.text_input("Confirm Password:", type="password", key="confirm_password")
        submit_button = st.sidebar.button("Submit", key="submit_button")
        cancel_button = st.sidebar.button("Cancel", key="cancel_button")

        if submit_button:
            # Validate form data (e.g., check for empty fields, password match)
            if new_username and new_email and new_phone_number and new_password and new_password == confirm_password:
                # Add logic to store new user data securely (replace with your actual storage mechanism)
                hashed_password = hash_password(new_password)
                user_data.append({
                    "username": new_username,
                    "email": new_email,
                    "phone_number": new_phone_number,
                    "password": hashed_password
                })
                st.sidebar.success("Account created successfully! Please log in.")
                st.session_state.creating_account = False
                st.experimental_rerun()
            else:
                st.sidebar.error("Please fill out all fields and ensure passwords match.")

        if cancel_button:
            st.session_state.creating_account = False
            st.experimental_rerun()

def authenticate_user(username, password):
    """
    Authenticates the user based on the provided username and password.
    """
    hashed_password = hash_password(password)  # Hash the entered password
    for user in user_data:
        if user["username"] == username and user["password"] == hashed_password:
            return True
    return False

def hash_password(password):
    """
    Hashes the provided password using a secure hashing algorithm.
    """
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashed_password

# Call the login_form function to display the login form
login_form()