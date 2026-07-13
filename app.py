import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
import tensorflow as tf
import pickle

model = tf.keras.models.load_model('model.h5')

with open('labelencoder_gender.pkl', 'rb') as f:
    label_encoder_gender= pickle.load(f)  

with open('scaler.pkl', 'rb') as f: 
    scaler = pickle.load(f)

with open('onehotencoder.pkl', 'rb') as f:
    onehot_encoder_geo = pickle.load(f)

st.title("Customer Churn Prediction")

geography = st.selectbox("Select Geography", ["France", "Spain", "Germany"])
gender = st.selectbox("Select Gender", ["Male", "Female"])
credit_score = st.number_input("Enter Credit Score")
age = st.number_input("Enter Age")
tenure = st.number_input("Enter Tenure")    
balance = st.number_input("Enter Balance")
estimated_salary = st.number_input("Enter Estimated Salary")
num_of_products = st.number_input("Enter Number of Products", 1, 4)
has_cr_card = st.selectbox("Has Credit Card?", [0,1])
is_active_member = st.selectbox("Is Active Member?", [0,1])


input_data = pd.DataFrame({
    'CreditScore': [credit_score],
    'Gender': [label_encoder_gender.transform([gender])[0]],
    'Age': [age],
    'Tenure': [tenure],
    'Balance': [balance],
    
    'NumOfProducts': [num_of_products],
    'HasCrCard': [has_cr_card],
    'IsActiveMember': [is_active_member],
    'EstimatedSalary': [estimated_salary]
})


one_hot_geo = onehot_encoder_geo.transform([[geography]]).toarray()
geo_df = pd.DataFrame(one_hot_geo, columns=onehot_encoder_geo.get_feature_names_out(['Geography']))

input_data= pd.concat([input_data.reset_index(drop=True), geo_df], axis=1)

input_data_scaled = scaler.transform(input_data)


prediction = model.predict(input_data_scaled)
prediction_proba = prediction[0][0]

if prediction_proba > 0.5:
    st.write("The customer is likely to churn.")        
else:
    st.write("The customer is unlikely to churn.")