import streamlit as st
import joblib
import xgboost
import pandas as pd

st.title('🎈 Aplicación de Machine Learning ')
st.info('Esta aplicación predice si un paciente se va a hospitalizar o no. Modifique las variables de entrada para obtener la predicción')
#st.text('Fixed width text')

with st.expander('Características'):
  #st.header('Ingrese las características')
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
  ordenesl=st.slider('Ordenes Laboratorio:',1, 10, 2)
  ordenesm=st.slider('Ordenes Microbiologia:',1, 10, 2)
  ordenesa=st.slider('Ordenes Ayudas:',1, 10, 2)
  ordenesi=st.slider('Ordenes Interconsulta:',1, 10, 2)
  especialidad = st.selectbox('Especialidad tratante', ('ALERGOLOGIA CLINICA','ALERGOLOGÍA PEDIÁTRICA',
                                                        'ANESTESIA','ANESTESIOLOGIA CARDIOVASCULAR',
                                                        'ANTIBIOTICOTERAPIA','CARDIOLOGIA - HEMODINAMIA',
                                                        'CIRUGIA GENERAL','MEDICO GENERAL'))
  totaldxurordenesa=st.slider('Total dx Urgencias:',1, 10, 3)
  nroatencionesprev=st.slider('Nro. atenciones prvias:',1, 10, 3)
  vivemed = st.selectbox('Vive en Medellín', ('Si', 'No'))
  ordencx = st.selectbox('Orden Cirugía', ('Si', 'No'))

# Cargo el modelo
model = joblib.load('production/models/pipeline_xgbv4.joblib')

# Defino las variables
cols_features=[
'Edad Ingreso',
'Sexo',
'Clasificacion Triaje',
'Causa Ingreso',
'Tipo Empresa',
'Ordenes Laboratorio',
'Ordenes Microbiologia',
'Ordenes Ayudas',
'Ordenes Interconsulta',
'Especialidad Tratante',
'Total Dx en Urgencias',
'Numero Atenciones Previas',
'Vive en Medellin',
'Orden Cirugia'
 ]
features=[(edad, genero, triaje, causa, tipoemp,ordenesl,ordenesm,ordenesa,ordenesi,especialidad, totaldxurordenesa,nroatencionesprev, vivemed,ordencx  )]
data_features=pd.DataFrame(data=features, columns=cols_features)

#st.subheader('Características ingresadas ')
data_features

# Realizo predicción
prediction=model.predict(data_features)
prediction_Percentage=model.predict_proba(data_features)
    
def return_predic(pred, p_pred):
    pr1=''
    if pred[0]==0: 
        pr1='No'
    else:
        pr1='Si'
    #return print(f"El paciente tiene una probabilidad del {p_pred[0,0]:.2%}  de {pr1} ser hospitalizado")
    return pr1

st.subheader('Predicción')
pr1=return_predic(prediction,prediction_Percentage)
st.info(f"El paciente tiene una probabilidad del {prediction_Percentage[0,0]:.2%}  de {pr1} ser hospitalizado")
  
