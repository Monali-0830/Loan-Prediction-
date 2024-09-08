import streamlit as st 
import numpy as np
import pickle 
import plotly.graph_objects as go 

def load_data():
    with open('model.pkl','rb') as file:
        data = pickle.load(file)
    return data   

model = load_data()

regressor = model['model']
le_gender = model['le_gender']
le_married = model['le_married']
le_employed = model['le_employed']
le_education = model['le_education']
le_dependent = model['le_dependent']
le_property_area =model['le_property_area']
    

def show_predict_page():
    st.title("Predictive Analytics for Loan Approval")

    st.write("### Help Us Predict Your Loan Approval Status")
    st.write("Kindly enter the following details to get an accurate estimate of your loan approval chances.")

    
    st.markdown("""
        <style>
            .stRadio > label, .stSelectbox > label, .stNumberInput > label, .stSlider > label {
            font-size: 18px; font-weight: 500; padding-top: 10px;
            }
            .stButton > button { 
                background-color: #4CAF50;
                color: white;
                font-size: 18px;
                font-weight: bold;
                border-radius: 8px;
                padding: 12px 24px;
                margin-top: 20px;
                width: 100%;
            }
            .stButton > button:hover {
                background-color: #45a049;
            }
            .header {
                font-size: 24px; color: #007BFF; font-weight: bold;
                margin-bottom: 15px;
            }
            .section {
                background-color: #f8f9fa;
                padding: 20px;
                border-radius: 10px;
                margin-bottom: 20px;
                box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
            }
            .divider {
                border-top: 2px solid #E6E6E6; margin: 30px 0;
            }
        </style>
    """, unsafe_allow_html=True)    


    st.title("🏦 Loan Application Form")

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # Organize the form into three columns with headers
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown('<div class="header">👤 Personal Info</div>', unsafe_allow_html=True)
        gender = st.radio("Gender", ["Male", "Female"])
        married = st.radio("Marital Status", ["Yes", "No"])
        dependents = st.select_slider("Dependents", options=["0", "1", "2", "3+"])
        education = st.radio("Education Level", ["Graduate", "Not Graduate"])

    with col2:
        st.markdown('<div class="header">💵 Financial Info</div>', unsafe_allow_html=True)
        self_employed = st.radio("Self Employed", ["Yes", "No"])
        applicant_income = st.number_input("Applicant Income", min_value=0, step=500, help="Enter your monthly income in USD.")
        coapplicant_income = st.number_input("Coapplicant Income", min_value=0, step=500, help="Enter the co-applicant's monthly income in USD.")
        loan_amount = st.number_input("Loan Amount Requested", min_value=0, step=500, help="Enter the loan amount in USD.")

    with col3:
        st.markdown('<div class="header">🏡 Loan Details</div>', unsafe_allow_html=True)
        loan_amount_term = st.slider("Loan Term (Months)", min_value=0, max_value=360, step=12, help="Choose the loan repayment term.")
        credit_history = st.radio("Credit History", ["No Issues", "Issues"], help="Select your credit history status.")
        property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"], help="Select the area where the property is located.")

    # Divider before the submit button
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    if st.button("Submit Application"):
        # Encode categorical variables
        gender_encoded = le_gender.transform([gender])[0]
        married_encoded = le_married.transform([married])[0]
        self_employed_encoded = le_employed.transform([self_employed])[0]
        education_encoded = le_education.transform([education])[0]
        dependents_encoded = le_dependent.transform([dependents])[0]
        property_area_encoded = le_property_area.transform([property_area])[0]

        # Encode credit history
        credit_history_encoded = 1 if credit_history == "No Issues" else 0

        # Create an array with all the inputs
        input_data = np.array([[gender_encoded, married_encoded, dependents_encoded, education_encoded,
                                self_employed_encoded, applicant_income, coapplicant_income,
                                loan_amount, loan_amount_term, credit_history_encoded, property_area_encoded]])

        # Make the prediction
        prediction = regressor.predict(input_data)

        # Display the result
        if prediction[0] == 1:
            st.success("🎉 Congratulations! Your loan application is likely to be approved.")
        else:
            st.error("🚫 Unfortunately, your loan application is likely to be denied.")
