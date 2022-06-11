from titanic_spaceship_package.param_grids.logistic_regression__v01 import param_grid_logistic_regression__v01
from titanic_spaceship_package.param_grids.knn__v01 import param_grid_knn__v01
from titanic_spaceship_package.param_grids.svm__v01 import param_grid_svm__v01
from titanic_spaceship_package.param_grids.logistic_regression__v02 import param_grid_logistic_regression__v02
from titanic_spaceship_package.param_grids.knn__v02 import param_grid_knn__v02
from titanic_spaceship_package.param_grids.svm__v02 import param_grid_svm__v02

def get_param_grid(model_name):
    
    if model_name == "logistic_regression__v01":
        param_grid = param_grid_logistic_regression__v01
    elif model_name == "knn__v01":
        param_grid = param_grid_knn__v01
    elif model_name == "svm__v01":
        param_grid = param_grid_svm__v01
    elif model_name == "logistic_regression__v02":
        param_grid = param_grid_logistic_regression__v02
    elif model_name == "knn__v02":
        param_grid = param_grid_knn__v02
    elif model_name == "svm__v02":
        param_grid = param_grid_svm__v02
    else:
        raise NotImplementedError
    
    return param_grid