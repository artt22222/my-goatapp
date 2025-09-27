import pandas as pd
import numpy as np
from collections import Counter
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV, StratifiedKFold, cross_val_predict
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, f1_score

# ---------------------- Load Data ----------------------
data = pd.read_csv("test/datadisease2.csv")
data.fillna(0, inplace=True)

X = data.drop('disease', axis=1)
y = data['disease']

le = LabelEncoder()
y_encoded = le.fit_transform(y)
n_classes = len(le.classes_)

# ---------------------- Compute Class Weights ----------------------
counter = Counter(y_encoded)
total = sum(counter.values())
class_weight = {cls: total/count for cls, count in counter.items()}
sample_weights = np.array([class_weight[yi] for yi in y_encoded])

# ---------------------- GridSearchCV ----------------------
param_grid = {
    "n_estimators": [100, 200],
    "max_depth": [3, 6],
    "learning_rate": [0.05, 0.1],
    "subsample": [1.0],
    "colsample_bytree": [0.8, 1.0],
    "gamma": [0, 1.0],
    "reg_alpha": [0, 1.0],
    "reg_lambda": [1.0, 2.0]
}

cv = StratifiedKFold(n_splits=8, shuffle=True, random_state=42)
grid_search = GridSearchCV(
    estimator=XGBClassifier(objective='multi:softprob', eval_metric='mlogloss', use_label_encoder=False),
    param_grid=param_grid,
    cv=cv,
    scoring="f1_macro",
    n_jobs=-1,
    verbose=1,
    return_train_score=True
)

grid_search.fit(X, y_encoded, sample_weight=sample_weights)
best_model = grid_search.best_estimator_

print("\n=== Best Parameters ===")
print(grid_search.best_params_)
print(f"Best CV f1_macro: {grid_search.best_score_:.4f}")

# ---------------------- Cross-Validation Prediction ----------------------
y_pred_cv = cross_val_predict(best_model, X, y_encoded, cv=cv)
print("\n=== Classification Report (CV) ===")
print(classification_report(y_encoded, y_pred_cv, target_names=le.classes_))

# ---------------------- Per-class Threshold Tuning ----------------------
y_bin = np.eye(n_classes)[y_encoded]  # one-hot encoding
probs = best_model.predict_proba(X)   # probability predictions

best_thresh = {}
for c in range(n_classes):
    best_f1 = 0
    best_t = 0.5
    for t in np.linspace(0.1, 0.9, 81):
        pred_c = (probs[:, c] >= t).astype(int)
        f1 = f1_score(y_bin[:, c], pred_c)
        if f1 > best_f1:
            best_f1 = f1
            best_t = t
    best_thresh[le.classes_[c]] = best_t

print("\n=== Optimal Threshold per Class ===")
print(best_thresh)

# ---------------------- Apply Thresholds for Final Prediction ----------------------
final_pred = np.zeros_like(probs)
for c, cls in enumerate(le.classes_):
    final_pred[:, c] = (probs[:, c] >= best_thresh[cls]).astype(int)

# Choose class with highest probability (one-hot to label)
final_pred_labels = final_pred.argmax(axis=1)
print("\n=== Final Classification Report (with Thresholds) ===")
print(classification_report(y_encoded, final_pred_labels, target_names=le.classes_))
