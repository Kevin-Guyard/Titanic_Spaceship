from titanic_spaceship_package.param_grids.logistic_regression__basic import param_grid_logistic_regression__basic
from titanic_spaceship_package.param_grids.knn__basic import param_grid_knn__basic
from titanic_spaceship_package.param_grids.svm__basic import param_grid_svm__basic
from titanic_spaceship_package.param_grids.logistic_regression__feature_selection import param_grid_logistic_regression__feature_selection
from titanic_spaceship_package.param_grids.knn__feature_selection import param_grid_knn__feature_selection
from titanic_spaceship_package.param_grids.svm__feature_selection import param_grid_svm__feature_selection

def get_param_grid(model_name):
    
    type_model = model_name.split("__v")[0]
    version = model_name.split("__v")[1]
    
    if type_model == "logistic_regression":
        
        if version in ["01"]:
            param_grid = param_grid_logistic_regression__basic
        elif version in ["02"]:
            param_grid = param_grid_logistic_regression__feature_selection
        else:
            raise NotImplementedError
            
    elif type_model == "knn":
        
        if version in ["01"]:
            param_grid = param_grid_knn__basic
        elif version in ["02"]:
            param_grid = param_grid_knn__feature_selection
        else:
            raise NotImplementedError
            
    elif type_model == "svm":
        
        if version in ["01"]:
            param_grid = param_grid_svm__basic
        elif version in ["02"]:
            param_grid = param_grid_svm__feature_selection
        else:
            raise NotImplementedError
            
    else:
        raise NotImplementedError
    
    return param_grid