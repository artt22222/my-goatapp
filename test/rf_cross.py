import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_predict, cross_val_score
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv("test/datadisease.csv")
data.fillna(0, inplace=True)

x = data.drop(['disease'], axis=1)
le = LabelEncoder()
y = data['disease']
y_encode = le.fit_transform(y)

model = RandomForestClassifier(n_estimators=300, random_state=42)

score = cross_val_score(model, x, y_encode,  cv=5)
print("Accuracy fold:", score)
print(f"Accuracy : {score.mean():.2f}")

y_pred = cross_val_predict(model, x, y_encode, cv= 5)
print(classification_report(y_encode, y_pred, target_names= le.classes_))