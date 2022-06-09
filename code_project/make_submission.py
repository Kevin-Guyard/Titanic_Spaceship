import kaggle
import os
import json
import pandas as pd

def make_submission(pipeline, model_name, repo_model, repo_submission, submit_on_kaggle, X_train, y_train, X_test, list_passenger_id):
    
    with open(os.path.join(repo_model, model_name + ".json"), 'r') as file:
        data = json.load(file)
        
    print("Model name: {}".format(data["model_name"]))
    print("Cross validation score: {}".format(data["best_score"]))
    print("Best params: {}".format(data["best_params"]))
    
    pipeline = pipeline.set_params(**data["best_params"])
    pipeline = pipeline.fit(X_train, y_train)
    y_pred = pipeline.predict(X_test)
    
    submission = pd.DataFrame({'PassengerId': list_passenger_id, 'Transported': y_pred})
    submission.to_csv(os.path.join(repo_submission, model_name + ".csv"), index=False)
    
    if submit_on_kaggle == True:
        
        path = os.path.join(repo_submission, model_name + ".csv")
        request = !kaggle competitions submit -c spaceship-titanic -f $path -m $model_name
        
        response = !kaggle competitions submissions -c spaceship-titanic --csv
        score_kaggle = float(response[2].split(',')[4])
        
        data["score_kaggle"] = score_kaggle
        
        with open(os.path.join(repo_model, model_name + ".json"), 'w+') as file:
            json.dump(data, file)
        
        print("Kaggle submission score: {}".format(score_kaggle))