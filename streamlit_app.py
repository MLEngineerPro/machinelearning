import streamlit as st
import joblib

st.title('🎈 Aplicación de Machine Learning ')
st.info('Esta aplicación predice si un paciente se va a hospitalizar o no.')
#st.text('Fixed width text')

with st.sidebar:
  st.header('Ingrese las características')
  edad=st.slider('Seleccione la edad:',1,120, 40)
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
  ordenenesl=st.slider('Ordenes Laboratorio:',1, 10, 2)
  ordenesm=st.slider('Ordenes Microbiologia:',1, 10, 2)
  ordenesa=st.slider('Ordenes Ayudas:',1, 10, 2)
  ordenesi=st.slider('Ordenes Interconsulta:',1, 10, 2)
  especialidad = st.selectbox('Especialidad tratante', ('ALERGOLOGIA CLINICA','ALERGOLOGÍA PEDIÁTRICA',
                                                        'ANESTESIA','ANESTESIOLOGIA CARDIOVASCULAR',
                                                        'ANTIBIOTICOTERAPIA','CARDIOLOGIA - HEMODINAMIA',
                                                        'CIRUGIA GENERAL','MEDICO GENERAL'))
  totaldxurordenesa=st.slider('Total dx Urgencias:',1, 10, 3)
  vivemed = st.selectbox('Vive en Medellín', ('Si', 'No'))
  ordencx = st.selectbox('Orden Cirugía', ('Si', 'No'))
  
  
  
