import pandas as pd

data = pd.read_csv('diabetes-dataset.csv')

data.head()

data.tail()

data.shape

print("Number of Rows",data.shape[0])
print("Number of Columns",data.shape[1])

data.info()

data.isnull().sum()

data.describe()

import numpy as np

data_copy = data.copy(deep=True)
data.columns

data_copy[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
       'BMI']] = data_copy[['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
       'BMI']].replace(0,np.nan)

data_copy.isnull().sum()

data['Glucose'] = data['Glucose'].replace(0,data['Glucose'].mean())
data['BloodPressure'] = data['BloodPressure'].replace(0,data['BloodPressure'].mean())
data['SkinThickness'] = data['SkinThickness'].replace(0,data['SkinThickness'].mean())
data['Insulin'] = data['Insulin'].replace(0,data['Insulin'].mean())
data['BMI'] = data['BMI'].replace(0,data['BMI'].mean())

X = data.drop('Outcome',axis=1)
y = data['Outcome']


import seaborn as sns

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20,
                                               random_state=42)
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingClassifier

from sklearn.pipeline import Pipeline
pipeline_lr  = Pipeline([('scalar1',StandardScaler()),
                         ('lr_classifier',LogisticRegression())])

pipeline_knn = Pipeline([('scalar2',StandardScaler()),
                          ('knn_classifier',KNeighborsClassifier())])

pipeline_svc = Pipeline([('scalar3',StandardScaler()),
                         ('svc_classifier',SVC())])
pipeline_rf = Pipeline([('rf_classifier',RandomForestClassifier(max_depth=9))])
pipeline_gbc = Pipeline([('gbc_classifier',GradientBoostingClassifier())])
pipelines = [pipeline_lr,
            pipeline_knn,
            pipeline_svc,
            pipeline_rf,
            pipeline_gbc]
pipelines

for pipe in pipelines:
    pipe.fit(X_train,y_train)

pipe_dict = {0:'LR',
             1:'KNN',
             2:'SVC',
             3: 'RF',
             4: 'GBC'}
pipe_dict

for i,model in enumerate(pipelines):
    print("{} Test Accuracy:{}".format(pipe_dict[i],model.score(X_test,y_test)*100))

from sklearn.ensemble import RandomForestClassifier
X = data.drop('Outcome',axis=1)
y = data['Outcome']
rf =RandomForestClassifier(max_depth=3)
rf.fit(X,y)
"""Prediction on New DATA"""
new_data = pd.DataFrame({
    'Pregnancies':6,
    'Glucose':148.0,
    'BloodPressure':72.0,
    'SkinThickness':35.0,
    'Insulin':79.799479,
    'BMI':33.6,
    'DiabetesPedigreeFunction':0.627,
    'Age':50,    
},index=[0])

accuracy_scores = []

for i, model in enumerate(pipelines):
    accuracy = model.score(X_test, y_test) * 100
    accuracy_scores.append(accuracy)