Loan Approval Prediction App

Overview

This is a machine learning project developed by Monali as the final project for an internship at Hoping Minds. The goal of this project is to predict loan approval based on various applicant features using a Random Forest Classifier. The application provides an interactive interface built with Streamlit for easy user interaction and data visualization.

Features

The project offers the following features:

✅ Loan Approval Prediction: Predicts the likelihood of loan approval based on user-provided input.
✅ Interactive Data Exploration: Users can explore and visualize loan application data through interactive charts and graphs.
✅ User-Friendly Interface: A simple and intuitive interface built with Streamlit for effortless interaction.
✅ Data Preprocessing: Includes data cleaning, handling missing values, and feature engineering to enhance model performance.
✅ Model Training & Evaluation: Utilizes a Random Forest Classifier trained on a preprocessed dataset for accurate predictions.
✅ Prediction Probability Visualization: Displays approval probability using an interactive gauge chart for better understanding.

Installation

Follow these steps to set up and run the application:

Clone the repository:

git clone https://github.com/jayash1973/Advanced-Loan-Predictor

Navigate to the project directory:

cd Advanced-Loan-Predictor

Install the required dependencies:

pip install -r requirements.txt

Usage

To start the application, run the following command:

streamlit run app.py

Once the app is running, open your web browser and navigate to:

http://localhost:8501

Modes of Operation

🔹 Predict Mode:

Fill in the required applicant information in the provided fields.

Click the "Predict" button to get the loan approval prediction and probability.

🔹 Explore Data Mode:

Explore various visualizations and insights from the loan application data, including:

Loan Status Distribution

Correlation Heatmap

Loan Amount Distribution

Applicant Income vs Loan Amount

Loan Status by Education and Credit History

Data

The project uses a loan application dataset (train.csv) for training and prediction. The dataset includes various features such as:

Gender

Marital Status

Education Level

Income

Loan Amount

Credit History

Model

The Random Forest Classifier was selected as the prediction model due to its:

✅ Ability to handle non-linear relationships in data
✅ High accuracy and robustness
✅ Capability of handling missing and categorical data effectively

Contributing

Contributions are welcome! If you have any suggestions, feel free to submit issues or pull requests.

Author

👩‍💻 Monali



Acknowledgments

A special thanks to Hoping Minds for providing the opportunity and mentorship throughout this project.

License

This project is licensed under the MIT License.

Contact

For any queries or further discussions, feel free to reach out:

