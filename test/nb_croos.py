import pandas as pd 
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.metrics import classification_report

data=  pd.read_csv("test/datadisease.csv")
data.fillna(0, inplace= True)

x = data.drop(['disease'], axis=1)
y =data['disease']

model = MultinomialNB(alpha=0.1)

score = cross_val_score(model, x, y, cv=5)
print("Accuracy Fold:",score)
print(f"Accuracy : {score.mean() :.2f}")

y_pred = cross_val_predict(model, x, y, cv=5)
print("Classification Report")
print(classification_report(y, y_pred))