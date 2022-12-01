import pickle
import pandas as pd
from getInputs import get_inputs
model = pickle.load(open("RandomForestClassifier_model.sav", "rb"))
_age = input("Enter your age: ")
_sex = input("Enter your gender: ")
_topo = input("Enter your topography: ")
_t = input("Enter your t: ")
_n = input("Enter your n: ")
_m = input("Enter your m: ")
_surge = input("Enter your surge: ")

model_params = get_inputs(_age, _sex, _topo, _t, _n, _m, _surge)
features=[pd.array(model_params)]
prediction = model.predict(features)
print(" The Current Colon Cancer Stage is ",prediction)
