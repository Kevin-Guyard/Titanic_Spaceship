import numpy as np

def get_param_iterator(model_name):
    
    version = model_name.split("__v")[1]
    
    if version in ["01"]:
        
        param_iterator = {
            "activate": False
        }
    
    elif version in ["02", "03", "04", "05", "06", "07", "10", "11", "12", "13", "14", "15"]:
        
        param_iterator = {
            "activate": True,
            "name_iterator": "feature_selection__k",
            "range_iterator": list(map(int, np.linspace(1, 3, 3)))
        }
        
    elif version in ["08", "09", "16", "17"]:
        
        param_iterator = {
            "activate": True,
            "name_iterator": "feature_selection__max_features",
            "range_iterator": list(map(int, np.linspace(1, 27, 27)))
        }
        
    elif version in ["18"]:
        
        param_iterator = {
            "activate": True,
            "name_iterator": "pca__n_components",
            "range_iterator": list(map(int, np.linspace(1, 28, 28)))
        }
        
    else:
        raise NotImplementedError
        
    return param_iterator