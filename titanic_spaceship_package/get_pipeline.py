from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression, RidgeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.feature_selection import SelectKBest, SelectFromModel, f_classif, mutual_info_classif
from sklearn.ensemble import RandomForestClassifier
from titanic_spaceship_package.preprocessor import preprocessor
from functools import partial

def get_pipeline(model_name, X_train, y_train):
    
    type_model = model_name.split("__v")[0]
    version = model_name.split("__v")[1]
    
    if version in ["01"]:
        
        steps = [
            ('preprocessor', preprocessor),
        ]
        
    elif version in ["02"]:
        
        steps = [
            ('preprocessor', preprocessor),
            ('feature_selection', SelectKBest(score_func=f_classif))
        ]
    
    elif version in ["03", "04", "05", "06", "07"]:
        
        discrete_mutual_info_classif = partial(mutual_info_classif, n_neighbors=int(version)-2)
        steps = [
            ('preprocessor', preprocessor),
            ('feature_selection', SelectKBest(score_func=discrete_mutual_info_classif))
        ]
    
    elif version in ["08"]:
        
        p = preprocessor
        X_train = p.fit_transform(X_train)
        rf = RandomForestClassifier(random_state=42, n_jobs=-1)
        rf = rf.fit(X_train, y_train)
        
        steps = [
            ('preprocessor', preprocessor),
            ('feature_selection', SelectFromModel(estimator=rf, threshold=0, prefit=True))
        ]
        
    elif version in ["09"]:
        
        p = preprocessor
        X_train = p.fit_transform(X_train)
        ridge = RidgeClassifier(random_state=42)
        ridge = ridge.fit(X_train, y_train)
        
        steps = [
            ('preprocessor', preprocessor),
            ('feature_selection', SelectFromModel(estimator=ridge, threshold=0, prefit=True))
        ]
        
    else:
        raise NotImplementedError

    if type_model == "logistic_regression":
        steps.append(
            ('logistic', LogisticRegression(max_iter=10000, random_state=42))
        )
    elif type_model == "knn":
        steps.append(
            ('knn', KNeighborsClassifier())
        )
    elif type_model == "svm":
        steps.append(
            ('svm', SVC(random_state=42))
        )
    else:
        raise NotImplementedError
        
    pipeline = Pipeline(steps=steps)
    
    return pipeline