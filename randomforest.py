import warnings
from sklearn.ensemble import RandomForestClassifier
warnings.filterwarnings('ignore')
import time
from sklearn.model_selection import RandomizedSearchCV,train_test_split
from sklearn.metrics import accuracy_score
import pickle
import pandas as pd

parmeters= {'bootstrap': [True, False],
               'max_depth': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, None],
               'max_features': ['auto', 'sqrt'],
               'min_samples_leaf': [1, 2, 4],
               'min_samples_split': [2, 5, 10],
               'n_estimators': [130, 180, 230]}
classification_model=RandomForestClassifier()
# Load the csv file
col_names = [['AGE','SEX','TOPOGRAPHY','T','N','M','SURGERY', 'STAGE']]
# load dataset
data = pd.read_csv("newdataset_classification1.csv")
feature_cols = ['AGE', 'SEX', 'TOPOGRAPHY', 'T', 'N', 'M', 'SURGERY']
X = data[feature_cols]  # Features
y = data.STAGE  # Target variable
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model_cv = RandomizedSearchCV(classification_model, parmeters, cv=5)
start=time.time()
model_cv.fit(X_train, y_train)
end=time.time()

filename = 'RandomForestClassifier_model.sav'
pickle.dump(model_cv, open(filename, 'wb'))
y_pred=model_cv.predict(X_test)
print("Accuracy = ",accuracy_score(y_test,y_pred))

