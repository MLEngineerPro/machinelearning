import streamlit as st
import joblib

st.title('🎈 Machine Learning App')
st.info('This app build a machine learning model')
st.text('Fixed width text')

with st.sidebar:
  st.header('Ingrese las características')
  st.slider('Seleccione la edad:',1,120, 40)
  genero = st.selectbox('Género', ('Masculino', 'Femenino', ''))
  triaje= st.selectbox('Triaje', ('1', '2', '3','4','5'))
  causa = st.selectbox('Causa ingreso', ('ENFERMEDAD GENERAL', 'ACCIDENTE OFIDICO',
                                         'ENFERMEDAD PROFESIONAL','ACCIDENTE DE TRABAJO',
                                         'ACCIDENTE DE TRANSITO','EVENTO CATASTROFICO',
                                         'SOSPECHA DE ABUSO SEXUAL'))
  tipoemp = st.selectbox('Tipo empresa', ('ENTES TERRITORIALES','ENTIDAD REGIMEN EXCEPC COMPART',
                                        'ENTIDADES REGIMEN DE EXCEPCION','E.P.S. REGIMEN CONTRIB COMPART',
                                        'E.P.S. REGIMEN CONTRIBUTIVO','E.P.S. REGIMEN SUBSID COMPARTI',
                                        'E.P.S. REGIMEN SUBSIDIADO','EXTRANJERO PERSONA JURIDICA',
                                        'EXTRANJERO PERSONA NATURAL','FOSYGA - ACCIDENT TTO - ECAT'))

  st.slider('Ordenes Laboratorio:',1, 10, 2)
  st.slider('Ordenes Microbiologia:',1, 10, 2)
  st.slider('Ordenes Ayudas:',1, 10, 2)
  st.slider('Ordenes Interconsulta:',1, 10, 2)

  
  
  
