from titanic_spaceship_package.param_grids.logistic_regression__basic import param_grid_logistic_regression__basic
from titanic_spaceship_package.param_grids.knn__basic import param_grid_knn__basic
from titanic_spaceship_package.param_grids.svm__basic import param_grid_svm__basic
from titanic_spaceship_package.param_grids.gnb__basic import param_grid_gnb__basic
from titanic_spaceship_package.param_grids.logistic_regression__feature_selection_kbest import param_grid_logistic_regression__feature_selection_kbest
from titanic_spaceship_package.param_grids.knn__feature_selection_kbest import param_grid_knn__feature_selection_kbest
from titanic_spaceship_package.param_grids.svm__feature_selection_kbest import param_grid_svm__feature_selection_kbest
from titanic_spaceship_package.param_grids.gnb__feature_selection_kbest import param_grid_gnb__feature_selection_kbest
from titanic_spaceship_package.param_grids.logistic_regression__feature_selection_from_model import param_grid_logistic_regression__feature_selection_from_model
from titanic_spaceship_package.param_grids.knn__feature_selection_from_model import param_grid_knn__feature_selection_from_model
from titanic_spaceship_package.param_grids.svm__feature_selection_from_model import param_grid_svm__feature_selection_from_model
from titanic_spaceship_package.param_grids.gnb__feature_selection_from_model import param_grid_gnb__feature_selection_from_model
from titanic_spaceship_package.param_grids.logistic_regression__pca import param_grid_logistic_regression__pca
from titanic_spaceship_package.param_grids.knn__pca import param_grid_knn__pca
from titanic_spaceship_package.param_grids.svm__pca import param_grid_svm__pca
from titanic_spaceship_package.param_grids.gnb__pca import param_grid_gnb__pca

def get_param_grid(model_name):
    
    type_model = model_name.split("__v")[0]
    version = model_name.split("__v")[1]
    
    if type_model == "logistic_regression":
        
        if version in ["01"]:
            param_grid = param_grid_logistic_regression__basic
        elif version in ["02", "03", "04", "05", "06", "07", "10", "11", "12", "13", "14", "15"]:
            param_grid = param_grid_logistic_regression__feature_selection_kbest
        elif version in ["08", "09", "16", "17"]:
            param_grid = param_grid_logistic_regression__feature_selection_from_model
        elif version in ["18"]:
            param_grid= param_grid_logistic_regression__pca
        else:
            raise NotImplementedError
            
    elif type_model == "knn":
        
        if version in ["01"]:
            param_grid = param_grid_knn__basic
        elif version in ["02", "03", "04", "05", "06", "07", "10", "11", "12", "13", "14", "15"]:
            param_grid = param_grid_knn__feature_selection_kbest
        elif version in ["08", "09", "16", "17"]:
            param_grid = param_grid_knn__feature_selection_from_model
        elif version in ["18"]:
            param_grid= param_grid_knn__pca
        else:
            raise NotImplementedError
            
    elif type_model == "svm":
        
        if version in ["01"]:
            param_grid = param_grid_svm__basic
        elif version in ["02", "03", "04", "05", "06", "07", "10", "11", "12", "13", "14", "15"]:
            param_grid = param_grid_svm__feature_selection_kbest
        elif version in ["08", "09", "16", "17"]:
            param_grid = param_grid_svm__feature_selection_from_model
        elif version in ["18"]:
            param_grid= param_grid_svm__pca
        else:
            raise NotImplementedError
            
    elif type_model == "gnb":
        
        if version in ["01"]:
            param_grid = param_grid_gnb__basic
        elif version in ["02", "03", "04", "05", "06", "07", "10", "11", "12", "13", "14", "15"]:
            param_grid = param_grid_gnb__feature_selection_kbest
        elif version in ["08", "09", "16", "17"]:
            param_grid = param_grid_gnb__feature_selection_from_model
        elif version in ["18"]:
            param_grid= param_grid_gnb__pca
        else:
            raise NotImplementedError
            
    else:
        raise NotImplementedError
    
    return param_grid