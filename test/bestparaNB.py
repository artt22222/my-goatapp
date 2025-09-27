import pandas as pd 
from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.naive_bayes import MultinomialNB
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, accuracy_score

data = pd.read_csv("test/datadisease4.csv")
data.fillna(0, inplace=True)

x = data.drop("disease", axis=1)
y = data["disease"]

le = LabelEncoder()
ylabel= le.fit_transform(y)


#set parameter
param_grid = {
    "alpha" : [0.1, 0.5, 1.0, 2.0],
    "fit_prior" : [True, False]
}

#set crossvaldation 
cv = StratifiedKFold(n_splits=5 , shuffle=True, random_state=42)
#set grid
grid_search = GridSearchCV(
    estimator= MultinomialNB(),
    param_grid= param_grid,
    cv=cv ,
    scoring = "f1_macro",
    n_jobs= -1,
    return_train_score= True
)

grid_search.fit(x, ylabel)

cv_results = pd.DataFrame(grid_search.cv_results_)

print("\n==Results for all Parameter==")
for i, row in cv_results.iterrows():
    params = row['params']
    f1_macro = row['mean_test_score']

    model = MultinomialNB(**params)
    model.fit(x, ylabel)
    y_pred_train= model.predict(x)
    acc = accuracy_score(ylabel, y_pred_train)

    print(f"set{i+1} : {params}")
    print(f" f1-score : {f1_macro:.4f}")
    print(f" Accuracy train : {acc:.4f}")
    print("-"*60)

print("/n Best Parameter :")
print(grid_search.best_params_)
print(f" Best f1-score : {grid_search.best_score_:.4f}")

# print("\n Classification Report best model")
# best_model = grid_search.best_estimator_
# y_pred_best = best_model.predict(x)
# print(classification_report(ylabel, y_pred_train, target_names=le.classes_))