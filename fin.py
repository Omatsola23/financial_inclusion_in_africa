#Import neccessary package
import pypickle as py
import streamlit as st
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
import numpy as np
#Add title and header to the app display
st.title("Financial Inclusion in Africa")
st.header("Know if an individual have a Bank Account")
#Load model from collab
model=py.load("lg.pkl")
#Give variable names to each input
user_input1=st.selectbox("Gender", ["","Male", "Female"])
user_input2=st.selectbox('Relationship with head of the house', ["","Head of household", "Spouse", "Child", "Sibling", "Friend","Other relatives"])
user_input3=st.selectbox("Job type",["","Self employed","Government dependent", "Retired", "Employed","Unemployed","Rural business(like fishing & farming)"])
user_input4=st.number_input("Age",format='%d', step=1)
#Calling out encoder for string input
label_encoder = LabelEncoder()
predictions1= label_encoder.fit_transform([user_input1])
predictions2= label_encoder.fit_transform([user_input2])
predictions3= label_encoder.fit_transform([user_input3])
predictionx=[[predictions1[0],predictions2[0],predictions3[0],user_input4]]
#Calling out the model for output
predictx = model.predict(predictionx)
#Output based on prediction
if st.button('ENTER'):
  if predictx==("Yes"):
    st.write("Individual have an account")
  else:
    st.write("Individual does not have an account")