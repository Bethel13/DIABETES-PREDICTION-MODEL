# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 07:24:40 2024

@author: HP
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json


app = FastAPI()

class model_input(BaseModel):
    
    Pregnancies : int
    Glucose : int
    BloodPressure : int
    SkinThickness : int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction : float
    Age : int
    
#loading the saved model

model = pickle.load(open('diabetes_model.sav','rb'))

@app.post('/diabetes_prediction')

def diabetes_pred(input_parameters : model_input):
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    preg = input_dictionary['Pregnancies']
    glu = input_dictionary['Glucose']
    bp = input_dictionary['BloodPressure']
    st = input_dictionary['SkinThickness']
    ins = input_dictionary['Insulin']
    bmi = input_dictionary['BMI']
    dpf = input_dictionary['DiabetesPedigreeFunction']
    age = input_dictionary['Age']
    
    input_list = [preg, glu, bp, st, ins, bmi, dpf, age]
    
    prediction = model.predict([input_list])
    
    if (prediction[0] == 0):
        return 'You are not diabetic, you are free to go.'
    else:
        return 'You are diabetic, you should visit a hospital!'
    