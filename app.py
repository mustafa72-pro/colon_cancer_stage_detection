import pandas as pd
from flask import Flask, request, jsonify, render_template,url_for
import pickle
from getInputs import get_inputs

app=Flask(__name__)

#loading the pickle model
model = pickle.load(open("RandomForestClassifier_model.sav", "rb"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route("/predict",methods =['POST'])
def predict():
    _age = request.form.get('AGE')
    _sex = request.form.get('SEX')
    _topo = request.form.get('TOPOGRAPHY')
    _t = request.form.get('T')
    _n = request.form.get('N')
    _m = request.form.get('M')
    _surge = request.form.get('SURGERY')
    model_params = get_inputs(_age,_sex,_topo,_t, _n,_m,_surge)
    features=[pd.array(model_params)]
    prediction = model.predict(features)
    accuracy = "0.90125"
    return render_template ("index.html",prediction_text= " The Current Colon Cancer Stage is {}".format(prediction))


if __name__ =="__main__":
    app.run(debug = True)
