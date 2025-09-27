import pandas as pd 
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV, StratifiedKFold, cross_val_predict
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score

data = pd.read_csv("test/datadisease4.csv")
data.fillna(0, inplace=True)

x= data.drop('disease', axis=1)
y= data['disease']

le= LabelEncoder()
ylabel = le.fit_transform(y)

param_grid = {
    "n_estimators" : [100, 200, 300],
    "max_depth" : [ 3, 6],
    "learning_rate" : [0.05, 0.1],
    "subsample" : [1.0],
    "colsample_bytree" : [0.8, 1.0],
    "gamma" : [0,1.0],
    "reg_alpha" : [0,1.0],
    "reg_lambda" : [1.0,2.0]
}

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

grid_search = GridSearchCV(
    estimator= XGBClassifier( eval_metric = 'mlogloss'),
    param_grid= param_grid,
    cv= cv,
    scoring= "f1_macro",
    n_jobs= -1,
    verbose= 1,
    return_train_score=True
)

grid_search.fit(x, ylabel)

cv_results = pd.DataFrame(grid_search.cv_results_)

print("\n=== Results for All Parameter===")
for i, row in cv_results.iterrows():
    params = row['params']
    f1_macro = row['mean_test_score']

    model= XGBClassifier(**params , eval_metric= 'mlogloss')
    model.fit(x, ylabel)
    ypred= model.predict(x)
    acc= accuracy_score(ylabel, ypred)

    print(f" Set{i+1} : {params}")
    print(f" f1-score : {f1_macro:.4f}")
    print(f" Accuracy : {acc:.4f}")

print("\n Best Parameters :")
print(grid_search.best_params_)
print(f" Best f1-score : {grid_search.best_score_:.4f}")

print("\n Classification Report")
best_model = grid_search.best_estimator_
ypred_best = cross_val_predict(best_model, x, ylabel, cv=cv )
print(classification_report(ylabel, ypred_best, target_names=le.classes_))