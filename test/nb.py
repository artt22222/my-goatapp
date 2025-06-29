import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

data = pd.read_csv("test/datadisease.csv")
data.fillna(0, inplace=True)
x = data.drop(['disease'], axis=1)
y = data['disease']


x_train, x_test, y_train, y_test = train_test_split(
    x,y,
    shuffle= True,
    test_size=0.3,
    random_state= 42,
    stratify= y 
)

model = MultinomialNB(alpha=0.1)
model.fit(x_train, y_train)

y_pred = model.predict(x_test)

acc = accuracy_score(y_test, y_pred)
print(f"Accuracy : {acc :.2f}")
print(classification_report(y_test,y_pred))
