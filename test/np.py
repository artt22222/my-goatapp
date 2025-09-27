import pandas as pd 
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_predict, StratifiedKFold
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, f1_score, precision_score, recall_score
from sklearn.preprocessing import LabelEncoder 

data=  pd.read_csv("test/datadisease2.csv")
data.fillna(0, inplace= True)

x = data.drop(['disease'], axis=1)
y =data['disease']
le = LabelEncoder()
y_encode = le.fit_transform(y)

model = MultinomialNB(alpha=2.0, fit_prior=True)

cv = StratifiedKFold(n_splits=5, shuffle= True, random_state=42)
y_pred = cross_val_predict(model, x, y_encode, cv=cv)

acc = accuracy_score(y_encode , y_pred)
pre = precision_score(y_encode, y_pred, average='macro')
rec = recall_score(y_encode, y_pred, average='macro')
f1 = f1_score(y_encode, y_pred, average='macro')

print("=== Report===")
print(f" Accuracy : {acc:.2%}")
print(f" Precision : {pre:.2%}")
print(f" Recall : {rec:.2%}")
print(f" F1-Score : {f1:.2%}")
print(classification_report(y_encode, y_pred, target_names=le.classes_))

print("\n=== Confusion Report Per Class ===")
cm = confusion_matrix(y_encode, y_pred)
class_names = le.classes_

for i, class_name in enumerate(class_names):
    TP = cm[i, i]
    FP = cm[:, i].sum() - TP
    FN = cm[i, :].sum() - TP
    TN = cm.sum() - (TP + FP + FN)

    print(f"\nClass: {class_name}")
    print(f"  True Positive  (TP): {TP}")
    print(f"  False Positive (FP): {FP}")
    print(f"  False Negative (FN): {FN}")
    print(f"  True Negative  (TN): {TN}")


# model.fit(x, y_encode)
# # jb.dump(model, 'test/RF_model.pkl')
# # jb.dump(le, 'test/label_encoder.pkl')