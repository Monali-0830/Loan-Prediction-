import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

@st.cache_data
def load_and_preprocess_data():
    data = pd.read_csv('train.csv')
    
    data['Gender'].fillna(data['Gender'].mode()[0], inplace=True)
    data['Married'].fillna(data['Married'].mode()[0], inplace=True)
    data['Dependents'].fillna(data['Dependents'].mode()[0], inplace=True)
    data['Self_Employed'].fillna(data['Self_Employed'].mode()[0], inplace=True)
    data['LoanAmount'].fillna(data['LoanAmount'].median(), inplace=True)
    data['Loan_Amount_Term'].fillna(data['Loan_Amount_Term'].mode()[0], inplace=True)
    data['Credit_History'].fillna(data['Credit_History'].mode()[0], inplace=True)
    
    data['Dependents'] = data['Dependents'].replace('3+', '3').astype(int)
    
    data['LoanAmount'] = np.log1p(data['LoanAmount'])
    data['ApplicantIncome'] = np.log1p(data['ApplicantIncome'])
    data['CoapplicantIncome'] = np.log1p(data['CoapplicantIncome'])
    
    return data

data = load_and_preprocess_data()

def show_explore_page():
    st.title("Loan Data Exploration")
    st.markdown("### An interactive analysis of loan data to understand trends and correlations.")
    
    # Loan Status Distribution
    st.subheader("1. Loan Status Distribution")
    st.markdown("This pie chart shows the distribution of loan approval status, giving a quick insight into the proportion of approved vs. rejected loans.")
    fig = px.pie(data, names='Loan_Status', title='Loan Status Distribution', hole=0.3,
                color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig, use_container_width=True)
        
    # Correlation Heatmap
    st.subheader("2. Correlation Heatmap")
    st.markdown("Explore the relationships between numeric features in the dataset with this heatmap. High correlation values might indicate multicollinearity.")
    numeric_cols = data.select_dtypes(include=[np.number]).columns
    corr_matrix = data[numeric_cols].corr()
    fig = px.imshow(corr_matrix, text_auto=True, aspect="auto", color_continuous_scale='RdBu')
    st.plotly_chart(fig, use_container_width=True)
        
    # Loan Amount Distribution
    st.subheader("3. Loan Amount Distribution")
    st.markdown("This histogram shows how loan amounts are distributed across different loans. It also highlights the loan status for each amount.")
    fig = px.histogram(data, x="LoanAmount", nbins=50, title="Loan Amount Distribution",
                    color="Loan_Status", color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig, use_container_width=True)
        
    # Applicant Income vs Loan Amount
    st.subheader("4. Applicant Income vs Loan Amount")
    st.markdown("This scatter plot visualizes the relationship between the applicant's income and the loan amount. It's useful to see if higher incomes correlate with higher loan amounts.")
    fig = px.scatter(data, x="ApplicantIncome", y="LoanAmount", color="Loan_Status",
                    title="Applicant Income vs Loan Amount",
                    color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig, use_container_width=True)
        
    # Loan Status by Education and Credit History
    st.subheader("5. Loan Status by Education and Credit History")
    st.markdown("This sunburst chart breaks down loan status based on education level and credit history. It helps in understanding how these factors influence loan approval.")
    fig = px.sunburst(data, path=['Education', 'Credit_History', 'Loan_Status'],
                    title="Loan Status by Education and Credit History",
                    color='Loan_Status', color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig, use_container_width=True)

    # Additional styling
    st.markdown("<style> .stSubheader { font-size: 20px; color: #007bff; } </style>", unsafe_allow_html=True)

