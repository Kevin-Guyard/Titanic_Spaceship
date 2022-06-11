from sklearn.model_selection import GridSearchCV
import json
import os

def hyperparameters_tuning(pipeline, param_grid, model_name, repo_model, X_train, y_train):
    
    clf = GridSearchCV(
        estimator=pipeline,
        param_grid=param_grid,
        scoring="accuracy",
        n_jobs=-1,
        refit=True,
        cv=5
    )
    
    clf = clf.fit(X_train, y_train)
    
    data = {
        "model_name": model_name,
        "best_score": clf.best_score_,
        "best_params": clf.best_params_,
        "time_to_tune": sum(clf.cv_results_["mean_fit_time"] + clf.cv_results_["mean_score_time"]) * clf.cv,
    }
    
    with open(os.path.join(repo_model, model_name + ".json"), "w+") as file:
        json.dump(data, file)