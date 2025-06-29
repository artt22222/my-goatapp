import pandas as pd 
from xgboost import XGBClassifier
from sklearn.model_selection import cross_val_predict, cross_val_score
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder 

data = pd.read_csv("test/datadisease.csv")
data.fillna(0, inplace= True)
x= data.drop('disease', axis= 1)
y= data['disease']

le= LabelEncoder()
y_encoded = le.fit_transform(y)

model = XGBClassifier(
    n_estimators = 200,
    max_depth = 6,
    learning_rate = 0.05,
    subsample= 0.8,
    colsample_bytree= 0.8,
    eval_metric= 'mlogloss',
    random_state= 42
)

scores = cross_val_score(model, x, y_encoded, cv=5)
print("Accuracy fold:", scores)
print("Accuracy mean : ", scores.mean())

y_pred = cross_val_predict(model, x, y_encoded, cv=5)
print("Classification Report")
print(classification_report(y_encoded, y_pred, target_names=le.classes_))