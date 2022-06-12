import sys
import os
import pandas as pd
from titanic_spaceship_package import get_pipeline, get_param_grid, hyperparameters_tuning
from datetime import datetime

start_time = datetime.now()

REPO_DATA_PREPROCESSED = 'data_preprocessed'
REPO_MODEL = 'model'
MODEL_NAME = sys.argv[1]

X_train = pd.read_csv(os.path.join(REPO_DATA_PREPROCESSED, "X_train.csv"))
y_train = pd.read_csv(os.path.join(REPO_DATA_PREPROCESSED, "y_train.csv")).Transported

pipeline = get_pipeline(model_name=MODEL_NAME)

param_grid = get_param_grid(model_name=MODEL_NAME)

hyperparameters_tuning(
    pipeline=pipeline,
    param_grid=param_grid,
    model_name=MODEL_NAME,
    repo_model=REPO_MODEL,
    X_train=X_train,
    y_train=y_train
)

end_time = datetime.now()
print(end_time - start_time)