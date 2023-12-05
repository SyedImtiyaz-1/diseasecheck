import joblib
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

cancer_model=pickle.load(open('cancer_model.pkl','rb'))
diabetes_model=joblib.load(open('diabetes_model.pkl','rb'))
heart_model=joblib.load(open('heart_model.pkl','rb'))
kidney_model=joblib.load(open('kidney_model.pkl','rb'))

# sidebar

with st.sidebar:
    selected=option_menu('Multiple Disease Detection System',['Welcome',
        'Cancer','Diabetes','Heart','Kidney'],
        icons=['book','bookmark-check','bi-app-indicator','heart','file-bar-graph','activity','bi-person'],
        default_index=0)

if selected == 'Welcome':
    st.title('Welcome to Automatic Disease Detection Using Machine Learning')
    st.image('disease-diagnosis-using-machine-learning.png')
    st.code("Developed by - Tushar Kumbhare, Rutuja Deshmukh, Isha Bisan, Namrata Anjankar")

if selected=='Cancer':
    st.title('Breast Cancer Test')
    concave=st.number_input('Concave',value=0.012,step=0.025)
    area=st.number_input('Area',value=500.0,step=0.1)
    radius=st.number_input('Radius',value=10.0,step=0.025)
    perimeter=st.number_input('Perimeter',value=60.0,step=0.1)
    concavity=st.number_input('Concavity',value=0.020470, step=0.025)

    result=''
    if st.button('Get result'):
        cancer_result=cancer_model.predict([[concave,area,radius,perimeter,concavity]])
        if cancer_result[0]==1:
            result='You are likely to have cancer. Please see a doctor.'
        else:
            result='You do not have cancer.'
    st.success(result)

if selected=='Diabetes':
    st.title('Diabetes Test')
    pregnancies=st.number_input('Number of pregnencies',min_value=0,max_value=10,step=1,value=1)
    glucose=st.number_input('Glucose Level',min_value=50,step=1,value=100)
    bp=st.number_input('Current blood Pressure',min_value=50,max_value=130,step=1,value=70)
    bmi=st.number_input('BMI',min_value=1,max_value=70,value=30,step=1)
    pedigree=st.number_input('Diabetes Pedigree Function',min_value=0.2,max_value=2.5,step=0.1,value=0.5)
    age=st.number_input('Age',min_value=0,max_value=100,step=1,value=18)

    result = ''
    if st.button('Get result'):
        diabetes_result = diabetes_model.predict([[pregnancies,glucose,bp,bmi,pedigree,age]])
        if diabetes_result[0] == 1:
            result = 'You are likely to have diabetes. Please see a doctor.'
        else:
            result = 'You do not have diabetes.'
    st.success(result)

if selected=='Heart':
    st.title('Heart Disease Test')
    chest_pain=st.selectbox('Chest Pain type',['Typical Angina','Atypical Angina', 'Non-Anginal Pain','Asymptomatic'])
    cp=int()
    if chest_pain=='Typical Angina':
        cp=0
    elif chest_pain=='Atypical Angina':
        cp=1
    elif chest_pain=='Non-Anginal Pain':
        cp=2
    else:
        cp=3
    rest_bp=st.number_input('Resting Blood Pressure (in mm of Hg)',value=120,step=1)
    cholestrol=st.number_input('Serum Cholestrol (in mg/dl)',value=200, step=5)
    blood_sugar=st.radio('Is Fasting Blood Sugar <120 mg/dl',['Yes','No'])
    ecg=st.selectbox('Electrocardiograph Result',['Normal','Having ST-T wave Abnormality','Showing propbable or definate left Ventricular Hypertrophy'])
    max_heart_rate=st.number_input('Maximum Heart Rate Achieved',value=150,step=1)
    exercise=st.selectbox('Exercise Induced Angina',['Yes','No'])

    result = ''
    if st.button('Get result'):
        heart_result = heart_model.predict([[cp,rest_bp,cholestrol,1 if blood_sugar=='Yes' else 0,0 if ecg=='Normal' else 1,max_heart_rate,1 if exercise=='Yes' else 0]])
        if heart_result[0] == 1:
            result = 'You are likely to have a heart disease. Please see a doctor.'
        else:
            result = 'Your heart is healthy.'
    st.success(result)

if selected=='Kidney':
    st.title('Kidney Test')
    bp=st.number_input('Blood Pressure',value=50,step=1)
    gravity=st.number_input('Specific Gravity',value=1.000,step=0.025)
    albumin=st.number_input('Albumin',value=1.0,step=0.5)
    sugar=st.number_input('Blood Sugar Level',value=1,step=1,max_value=5)
    rbc=st.radio('Red Blood Cells Count',['abnormal','normal'])
    pbc=st.radio('Pus Cell Count',['abnormal','normal'])
    pcclumps=st.radio('Pus Cell Clumps',['present','not present'])

    result = ''
    if st.button('Get result'):
        kidney_result = kidney_model.predict([[bp,gravity,albumin,sugar,1 if rbc=='abnormal' else 0,1 if pbc=='abnormal' else 1,1 if pcclumps=='present' else 0]])
        if kidney_result[0] == 1:
            result = 'You are likely to have a kidney disease. Please see a doctor.'
        else:
            result = 'Your kidney is healthy.'
    st.success(result)
