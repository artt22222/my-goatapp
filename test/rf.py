import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

data = pd.read_csv("test/datadisease.csv")
data.fillna(0, inplace=True)

x = data.drop(['disease'], axis=1)
y = data['disease']

x_train, x_test, y_train, y_test = train_test_split(
    x,y,
    test_size=0.3,
    shuffle=True,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(x_train, y_train)

y_pred= model.predict(x_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred) :.2f}")
print("Classification Report")
print(classification_report(y_test, y_pred))