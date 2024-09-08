import streamlit as st
from explore_page import show_explore_page
from predict_page import show_predict_page


st.sidebar.header("🧭 Navigation")

selectionpart = st.sidebar.radio("Select a Page",['🔮 Predict Loan Approval','📊 Explore Data'])

st.sidebar.markdown("---")  # Add a horizontal divider
st.sidebar.text("Powered by Streamlit")

if selectionpart == '🔮 Predict Loan Approval':
    show_predict_page()
else:
    show_explore_page()


