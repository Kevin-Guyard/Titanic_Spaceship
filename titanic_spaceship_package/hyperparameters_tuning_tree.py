from sklearn.model_selection import RandomizedSearchCV
import json
import os

def hyperparameters_tuning_tree(pipeline, param_distrib, param_iterator, model_name, repo_model, X_train, y_train):
    
    if param_iterator["activate"] == True:
        
        best_score = 0
        best_params = None
        best_value_iterator = None
        time_to_tune = 0
        
        for value_iterator in param_iterator["range_iterator"]:
            
            pipeline.set_params(**{param_iterator["name_iterator"]: value_iterator})
    
            clf = RandomizedSearchCV(
                estimator=pipeline,
                param_distributions=param_distrib,
                n_iter=200,
                scoring='accuracy',
                refit=False,
                cv=5,
                random_state=42,
                n_jobs=-1
            )

            clf = clf.fit(X_train, y_train)
            
            time_to_tune += sum(clf.cv_results_["mean_fit_time"] + clf.cv_results_["mean_score_time"]) * clf.cv
            
            if clf.best_score_ > best_score:
                best_score = clf.best_score_
                best_params = clf.best_params_
                best_params.update({param_iterator["name_iterator"]: value_iterator})
                
        data = {
            "model_name": model_name,
            "best_score": best_score,
            "best_params": best_params,
            "time_to_tune": time_to_tune
        }   
        
    else:
        
        clf = RandomizedSearchCV(
            estimator=pipeline,
            param_distributions=param_distrib,
            n_iter=200,
            scoring='accuracy',
            refit=False,
            cv=5,
            random_state=42,
            n_jobs=-1
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