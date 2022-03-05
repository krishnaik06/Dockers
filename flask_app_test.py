# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 18:02:42 2022

@author: darkf
"""
from flask import Flask,request
import pandas as pd
import numpy as np
import pickle


app=Flask(__name__)#Which point you are goin to start
pickle_in=open('classifier.pkl','rb')
classifier=pickle.load(pickle_in)

#root path
@app.route('/')
def welcome():
    return "Welcome All"

@app.route('/predict')
def predict_note_authentication():
    variance=request.args.get('variance')
    skewness=request.args.get('skewness')
    curtosis=request.args.get('curtosis')
    entropy=request.args.get('entropy')
    prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
    return "The predicted values is"+str(prediction)


@app.route('/predict_file',methods=["POST"])
def predict_note_file():
    df_test=pd.read_csv(request.files.get("file"))
    prediction=classifier.predict(df_test)
    
    return "The predicted values of csv are"+str(list(prediction))

if __name__=='__main__':
    app.run()
    