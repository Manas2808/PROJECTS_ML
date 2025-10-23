import streamlit as st
import pickle
import numpy as np

# load model 
with open("log_model.pkl",'rb') as f:
    model = pickle.load(f)

# Load Encoder
with open("sex_encoder.pkl",'rb') as f:
    sex_enc = pickle.load(f)

with open("emb_encoder.pkl",'rb') as f:
    emb_enc = pickle.load(f)

# # Set UI title
st.title("Titanic Survival Prediction")

sex_option = list(sex_enc.classes_)
emb_option = list(emb_enc.classes_)
psngr_class = [1,2,3]
# user input

Pclass = st.selectbox("Passenger Class",psngr_class)
sex  = st.selectbox("Passenger Sex",sex_option)
Age = st.slider("Passenger Age",min_value=0,max_value=80,)
Fare = st.number_input("Fair Paid",min_value=0)
Embarked = st.selectbox("Embarked",emb_option)
