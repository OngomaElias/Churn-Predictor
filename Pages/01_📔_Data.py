import streamlit as st
import pyodbc
import pandas as pd

st.set_page_config(
    page_title='Data Page',
    page_icon='📔',
    layout='wide'
)

st.title('Telcom Churn Database 📔')

# Create a connection to the database
@st.cache_resource(show_spinner='Connecting to database ...')
def init_connection():
    return pyodbc.connect(
        "DRIVER={SQL Server};SERVER="
        + st.secrets['SERVER_NAME']
        + ";DATABASE="
        + st.secrets['DATABASE_NAME']
        + ";UID="
        + st.secrets['USER']
        + ";PWD="
        + st.secrets['PASSWORD']
    )

# Initialize the connection
connection = init_connection()

@st.cache_data(show_spinner='Running query ...')
def running_query(query):
    with connection.cursor() as c:
        c.execute(query)
        rows = c.fetchall()
        df = pd.DataFrame.from_records(rows, columns=[column[0] for column in c.description])
    return df

def get_all_columns():
    sql_query = "SELECT * FROM " + st.secrets['TABLE_NAME']
    df = running_query(sql_query)
    return df

# Load data once and use it in the session state
if 'dataframe' not in st.session_state:
    st.session_state.dataframe = get_all_columns()

df = st.session_state.dataframe

# Determine numerical and categorical columns
numerical_columns = df.select_dtypes(include=['number']).columns.tolist()
categorical_columns = df.select_dtypes(exclude=['number']).columns.tolist()

# Create a selectbox for column type selection
column_type = st.selectbox('Select column type to display:', ('All Columns', 'Numerical', 'Categorical'))

# Display the appropriate columns based on selection
if column_type == 'Numerical':
    st.write("Numerical Columns:")
    st.write(df[numerical_columns])
elif column_type == 'Categorical':
    st.write("Categorical Columns:")
    st.write(df[categorical_columns])
else:
    st.write("All Columns:")
    st.write(df)

# Section to learn about features
st.header('Learn About Features')

data = {
    'Customer Data': {
        'customerID': {'Description': 'Unique identifier for each customer', 'Type': 'String'},
        'gender': {'Description': 'Gender of the customer', 'Type': 'String', 'Possible Values': ['Male', 'Female']},
        'SeniorCitizen': {'Description': 'Indicates if the customer is a senior citizen', 'Type': 'Boolean', 'Possible Values': [True, False]},
        'Partner': {'Description': 'Indicates if the customer has a partner', 'Type': 'Boolean', 'Possible Values': [True, False]},
        'Dependents': {'Description': 'Indicates if the customer has dependents', 'Type': 'Boolean', 'Possible Values': [True, False]},
        'tenure': {'Description': 'Number of months the customer has been with the company', 'Type': 'Integer'},
        'PhoneService': {'Description': 'Indicates if the customer has phone service', 'Type': 'Boolean', 'Possible Values': [True, False]},
        'MultipleLines': {'Description': 'Indicates if the customer has multiple lines', 'Type': 'String', 'Possible Values': ['Yes', 'No', 'No phone service']},
        'InternetService': {'Description': 'Type of internet service', 'Type': 'String', 'Possible Values': ['DSL', 'Fiber optic', 'No']},
        'OnlineSecurity': {'Description': 'Indicates if the customer has online security', 'Type': 'String', 'Possible Values': ['Yes', 'No', 'No internet service']},
        'DeviceProtection': {'Description': 'Indicates if the customer has device protection', 'Type': 'String', 'Possible Values': ['Yes', 'No', 'No internet service']},
        'TechSupport': {'Description': 'Indicates if the customer has tech support', 'Type': 'String', 'Possible Values': ['Yes', 'No', 'No internet service']},
        'StreamingTV': {'Description': 'Indicates if the customer has streaming TV', 'Type': 'String', 'Possible Values': ['Yes', 'No', 'No internet service']},
        'StreamingMovies': {'Description': 'Indicates if the customer has streaming movies', 'Type': 'String', 'Possible Values': ['Yes', 'No', 'No internet service']},
        'Contract': {'Description': 'Type of contract', 'Type': 'String', 'Possible Values': ['Month-to-month', 'One year', 'Two year']},
        'PaperlessBilling': {'Description': 'Indicates if the customer has paperless billing', 'Type': 'Boolean', 'Possible Values': [True, False]},
        'PaymentMethod': {'Description': 'Payment method', 'Type': 'String', 'Possible Values': ['Electronic check', 'Mailed check', 'Bank transfer (automatic)', 'Credit card (automatic)']},
        'MonthlyCharges': {'Description': 'Monthly charges', 'Type': 'Float'},
        'TotalCharges': {'Description': 'Total charges', 'Type': 'Float'},
        'Churn': {'Description': 'Indicates if the customer churned', 'Type': 'Boolean', 'Possible Values': [True, False]}
    }
}

with st.expander('View Data'):
    st.subheader('Customer Data')
    for key, value in data['Customer Data'].items():
        st.write(f"- **{key}**")
        st.write(f"  - Description: {value['Description']}")
        st.write(f"  - Type: {value['Type']}")
        if 'Possible Values' in value:
            st.write(f"  - Possible Values: {value['Possible Values']}")

# Create a selectbox for column selection to learn more
st.header('Learn More About Specific Feature')

selected_feature = st.selectbox('Select a feature to learn more:', list(data['Customer Data'].keys()))

feature_info = data['Customer Data'][selected_feature]

st.write(f"**{selected_feature}**")
st.write(f"- Description: {feature_info['Description']}")
st.write(f"- Type: {feature_info['Type']}")
if 'Possible Values' in feature_info:
    st.write(f"- Possible Values: {feature_info['Possible Values']}")
