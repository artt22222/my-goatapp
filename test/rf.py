import pandas as pd
import numpy as np
import joblib as jb
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_predict, StratifiedKFold
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import (
    confusion_matrix, accuracy_score, precision_score, recall_score,
    f1_score, classification_report
)

# =======================
# 1) Load & preprocess data
# =======================
data = pd.read_csv("datadisease4.csv")
data.fillna(0, inplace=True)

# Features & Labels
feature_names = data.drop(['disease'], axis=1).columns.tolist()
x = data.drop(['disease'], axis=1).values
y = data['disease']

# Label Encoding
le = LabelEncoder()
y_encode = le.fit_transform(y)

print("Features used for training:", len(feature_names))
print(feature_names)

# =======================
# 2) Model & Cross-validation
# =======================
model = RandomForestClassifier(
    n_estimators=300,
    random_state=42,
    class_weight='balanced',
    max_depth=20,
    min_samples_leaf=1,
    min_samples_split=4
)

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
y_pred = cross_val_predict(model, x, y_encode, cv=cv)

# =======================
# 3) Evaluation
# =======================
acc = accuracy_score(y_encode, y_pred)
pre = precision_score(y_encode, y_pred, average='macro')
rec = recall_score(y_encode, y_pred, average='macro')
f1 = f1_score(y_encode, y_pred, average='macro')

print("=== Report ===")
print(f" Accuracy : {acc:.2%}")
print(f" Precision : {pre:.2%}")
print(f" Recall    : {rec:.2%}")
print(f" F1-Score  : {f1:.2%}")
print(classification_report(y_encode, y_pred, target_names=le.classes_))

# Confusion Matrix
cm = confusion_matrix(y_encode, y_pred)
class_names = le.classes_

plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues",
            xticklabels=class_names, yticklabels=class_names)
plt.title("Confusion Matrix", fontsize=16)
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()

# Per-class metrics bar chart
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
plt.ylim(0, 1.20)
plt.legend(loc="lower right")

colors = ["tab:blue", "tab:orange", "tab:green"]

for i, container in enumerate(ax.containers):
    for bar in container:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.01,
            f"{height:.2f}",
            ha="center",
            va="bottom",
            fontsize=9,
            color=colors[i],
            fontweight="bold",
            rotation=90
        )

plt.show()

# =======================
# 4) Train Final Model & Save
# =======================
print("\nTraining final model on all data...")
model.fit(x, y_encode)

jb.dump(model, "modelRf.pkl")
jb.dump(le, "newlabel_encoder.pkl")
jb.dump(feature_names, "feature_names.pkl")

print("✅ Model, encoder, and feature names saved successfully!")
