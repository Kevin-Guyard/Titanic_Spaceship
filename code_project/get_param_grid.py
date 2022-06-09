from code_project.param_grid.logistic_regression__v01 import param_grid_logistic_regression__v01
from code_project.param_grid.knn__v01 import param_grid_knn__v01
from code_project.param_grid.svm__01 import param_grid_svm__01

def get_param_grid(model_name):
    
    if model_name == "logistic_regression__v01":
        param_grid = param_grid_logistic_regression__v01
    elif model_name == "knn__v01":
        param_grid = param_grid_knn__v01
    elif model_name == "svm__v01":
        param_grid = param_grid_svm__v01
    else:
        raise NotImplementedError
    
    return param_grid