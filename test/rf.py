import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_predict, GridSearchCV, StratifiedKFold
from sklearn.metrics import (
    confusion_matrix, accuracy_score, precision_score, f1_score, recall_score,classification_report
)
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix
import joblib as jb
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



data = pd.read_csv("test/datadisease4.csv")
data.fillna(0, inplace=True)

x = data.drop(['disease'], axis=1).values
le = LabelEncoder()
y = data['disease']
y_encode = le.fit_transform(y)

model = RandomForestClassifier(n_estimators=200, random_state=42, class_weight= 'balanced', max_depth=None, min_samples_leaf=1, min_samples_split= 2)

cv = StratifiedKFold(n_splits=10, shuffle= True, random_state=42)
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
    
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", 
            xticklabels=class_names, yticklabels=class_names)
plt.title("Confusion Matrix", fontsize=16)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

report = classification_report(
    y_encode, y_pred, target_names=class_names, output_dict=True
)
metrics_df = pd.DataFrame(report).transpose().drop(
    ['accuracy', 'macro avg', 'weighted avg']
)

ax = metrics_df[['precision', 'recall', 'f1-score']].plot(
    kind="bar", figsize=(12, 6), rot=45
)

plt.title("Precision / Recall / F1 per Class", fontsize=16)
plt.ylabel("Score")
plt.ylim(0, 1.20)  # เผื่อพื้นที่ด้านบน
plt.legend(loc="lower right")

# สีเดียวกับแท่ง
colors = ["tab:blue", "tab:orange", "tab:green"]

# ใส่ตัวเลขบนแท่งแบบแนวตั้ง
for i, container in enumerate(ax.containers):
    for bar in container:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.01,            # วางเหนือแท่งนิดหน่อย
            f"{height:.2f}",
            ha="center",
            va="bottom",
            fontsize=9,
            color=colors[i],
            fontweight="bold",
            rotation=90               # หมุนเป็นแนวตั้ง
        )

plt.show()

# model.fit(x, y_encode)
# jb.dump(model, 'test/RF_model.pkl')
# jb.dump(le, 'test/label_encoder.pkl')
