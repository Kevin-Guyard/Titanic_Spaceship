import numpy as np

def get_param_distrib(model_name):
    
    type_model = model_name.split("__v")[0]
    
    if type_model == "random_forest":
        
        param_distrib = {
            "random_forest__n_estimators": list(map(int, np.linspace(100, 1000, 10))),
            "random_forest__max_depth": list(map(int, np.linspace(10, 100, 10))),
            "random_forest__min_samples_split": list(map(int, np.linspace(2, 10, 9))),
            "random_forest__min_samples_leaf": list(map(int, np.linspace(1, 5, 5))),
            "random_forest__bootstrap": [True, False],
        }
    
    else:
        raise NotImplementedError
        
    return param_distrib