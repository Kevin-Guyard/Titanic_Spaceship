import sys
import os
import pandas as pd
from titanic_spaceship_package import get_pipeline, get_param_grid, hyperparameters_tuning_classic, hyperparameters_tuning_tree, get_param_distrib, get_param_iterator
from datetime import datetime

start_time = datetime.now()

REPO_DATA_PREPROCESSED = 'data_preprocessed'
REPO_MODEL = 'model'
MODEL_NAME = sys.argv[1]

X_train = pd.read_csv(os.path.join(REPO_DATA_PREPROCESSED, "X_train.csv"))
y_train = pd.read_csv(os.path.join(REPO_DATA_PREPROCESSED, "y_train.csv")).Transported

pipeline = get_pipeline(model_name=MODEL_NAME)

type_model = MODEL_NAME.split("__v")[0]

if type_model in ["logistic_regression", "knn", "svm", "gnb"]:

    param_grid = get_param_grid(model_name=MODEL_NAME)

    hyperparameters_tuning_classic(
        pipeline=pipeline,
        param_grid=param_grid,
        model_name=MODEL_NAME,
        repo_model=REPO_MODEL,
        X_train=X_train,
        y_train=y_train
    )
    
elif type_model in ["random_forest"]:
    
    param_distrib = get_param_distrib(model_name=MODEL_NAME)
    param_iterator = get_param_iterator(model_name=MODEL_NAME)
    
    hyperparameters_tuning_tree(
        pipeline=pipeline,
        param_distrib=param_distrib,
        param_iterator=param_iterator,
        model_name=MODEL_NAME,
        repo_model=REPO_MODEL,
        X_train=X_train,
        y_train=y_train
    )

end_time = datetime.now()
print(end_time - start_time)