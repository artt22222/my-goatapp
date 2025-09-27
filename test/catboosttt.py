# === STEP 0: ติดตั้ง catboost ถ้ายังไม่ได้ติดตั้ง ===
# pip install catboost

import pandas as pd
from catboost import CatBoostClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold, GridSearchCV

# === Load dataset ===
df = pd.read_csv("test/datadisease2.csv")
df.fillna(0, inplace=True)

X = df.drop("disease", axis=1)
y = df["disease"]

le = LabelEncoder()
y_encoded = le.fit_transform(y)

# === Define parameter grid ===
param_grid = {
    'depth': [6, 8, 10],
    'learning_rate': [0.05, 0.1, 0.2],
    'iterations': [300, 400, 500],
    'l2_leaf_reg': [1, 3, 5]
}

# === Setup cross-validation ===
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

# === GridSearchCV ===
cat_model = CatBoostClassifier(
    loss_function='MultiClass',
    eval_metric='TotalF1',
    auto_class_weights='Balanced',
    random_seed=42,
    verbose=0
)

grid_search = GridSearchCV(
    estimator=cat_model,
    param_grid=param_grid,
    scoring='f1_macro',
    cv=cv,
    n_jobs=-1,
    verbose=1
)

grid_search.fit(X, y_encoded)

print("=== Best Parameters ===")
print(grid_search.best_params_)
print("Best macro F1:", grid_search.best_score_)

from catboost import CatBoostClassifier, Pool
from sklearn.model_selection import StratifiedKFold, cross_val_predict
from sklearn.metrics import classification_report, confusion_matrix

# ใช้พารามิเตอร์ดีที่สุดจาก grid_search
best_params = grid_search.best_params_

cat_model_final = CatBoostClassifier(
    iterations=best_params['iterations'],
    depth=best_params['depth'],
    learning_rate=best_params['learning_rate'],
    l2_leaf_reg=best_params['l2_leaf_reg'],
    loss_function='MultiClass',
    eval_metric='TotalF1',
    auto_class_weights='Balanced',
    random_seed=42,
    verbose=100
)

# Cross-validation 10-fold
cv = StratifiedKFold(n_splits=10, shuffle=True, random_state=42)
y_pred_cv = cross_val_predict(cat_model_final, X, y_encoded, cv=cv, n_jobs=-1)

# Classification report
print("\n=== Classification Report (CV) ===")
print(classification_report(y_encoded, y_pred_cv, target_names=le.classes_))

# Confusion matrix
cm = confusion_matrix(y_encoded, y_pred_cv)
print("\n=== Confusion Matrix ===")
print(cm)

# Train final model on all data
# cat_model_final.fit(X, y_encoded)
# cat_model_final.save_model("catboost_goat_disease_best.cbm")
