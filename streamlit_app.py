import streamlit as st
import joblib

st.title('🎈 Machine Learning App')
st.info('This app build a machine learning model')
st.text('Fixed width text')

st.select_slider('Selecciones la edad', options=[1,'2'])
