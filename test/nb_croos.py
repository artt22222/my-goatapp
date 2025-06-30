import pandas as pd 
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.metrics import classification_report
from sklearn.preprocessing import LabelEncoder 

data=  pd.read_csv("test/datadisease.csv")
data.fillna(0, inplace= True)

x = data.drop(['disease'], axis=1)
y =data['disease']
le = LabelEncoder()
y_encode = le.fit_transform(y)

model = MultinomialNB(alpha=0.1)

score = cross_val_score(model, x, y_encode, cv=5)
print("Accuracy Fold:",score)
print(f"Accuracy : {score.mean() :.2f}")

y_pred = cross_val_predict(model, x, y_encode, cv=5)
print("Classification Report")
print(classification_report(y_encode, y_pred, target_names=le.classes_))