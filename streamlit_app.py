# 
import streamlit as st
import pandas as pd
import pickle as pk

data = pd.read_csv('./response.csv') 
st.title("Begaluru House Price Prediction")

selected_location = st.selectbox("Select Location",data['location'].unique(),index=None)
selected_bhk = st.selectbox("Select BHK",data['bhk'].unique().astype(int),index=None)
selected_bath = st.selectbox("Select Bathroom",data['bath'].unique().astype(int),index=None)
selected_sqft = st.selectbox("Select Square Feet Area",data['total_sqft'].unique().astype(int),index=None)

if 'ans' not in st.session_state:
    st.session_state['ans'] = False 

def eval_price():
    try:
        pipe = pk.load(open('./model.pkl','rb'))
        val = pipe.predict([[selected_location,selected_sqft.astype(float),selected_bath.astype(float),selected_bhk.astype(float)]])
        st.write(f"Predicted Price: ${val[0].astype(int)} Lakh")
    except :
        st.write('Error select all option')


col1, col2 = st.columns([1,1])
with col2:
    st.button("Reset")
with col1:
    if st.button('Predict'):
        eval_price()
    else:
        st.write('')
