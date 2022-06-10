from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from titanic_spaceship_package.preprocessor import preprocessor

def get_pipeline(model_name):
    
    if model_name.split("__v")[1] == "01":
        steps = [
            ('preprocessor', preprocessor),
        ]
    else:
        raise NotImplementedError
    
    if "logistic_regression" in model_name:
        steps.append(
            ('logistic', LogisticRegression(max_iter=1000, random_state=42))
        )
    elif "knn" in model_name:
        steps.append(
            ('knn', KNeighborsClassifier())
        )
    elif "svm" in model_name:
        steps.append(
            ('svm', SVC(random_state=42))
        )
    else:
        raise NotImplementedError
        
    pipeline = Pipeline(steps=steps)
    
    return pipeline