from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression, RidgeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.feature_selection import SelectKBest, SelectFromModel, f_classif, mutual_info_classif
from sklearn.ensemble import RandomForestClassifier
from sklearn.decomposition import PCA
from titanic_spaceship_package.preprocessor import preprocessor
from functools import partial

def get_pipeline(model_name):
    
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
        
        steps = [
            ('preprocessor', preprocessor),
            ('feature_selection', SelectFromModel(estimator=RandomForestClassifier(random_state=42, n_jobs=-1), threshold=0, prefit=False))
        ]
        
    elif version in ["09"]:
        
        steps = [
            ('preprocessor', preprocessor),
            ('feature_selection', SelectFromModel(estimator=RidgeClassifier(random_state=42), threshold=0, prefit=False))
        ]
        
    elif version in ["10"]:
        
        steps = [
            ('preprocessor', preprocessor),
            ('feature_selection', SelectKBest(score_func=f_classif)),
            ('pca', PCA(random_state=42))
        ]
        
    elif version in ["11", "12", "13", "14", "15"]:
        
        discrete_mutual_info_classif = partial(mutual_info_classif, n_neighbors=int(version)-10)
        steps = [
            ('preprocessor', preprocessor),
            ('feature_selection', SelectKBest(score_func=discrete_mutual_info_classif)),
            ('pca', PCA(random_state=42))
        ]
        
    elif version in ["16"]:
        
        steps = [
            ('preprocessor', preprocessor),
            ('feature_selection', SelectFromModel(estimator=RandomForestClassifier(random_state=42, n_jobs=-1), threshold=0, prefit=False)),
            ('pca', PCA(random_state=42))
        ]
        
    elif version in ["17"]:
        
        steps = [
            ('preprocessor', preprocessor),
            ('feature_selection', SelectFromModel(estimator=RidgeClassifier(random_state=42), threshold=0, prefit=False)),
            ('pca', PCA(random_state=42))
        ]
        
    elif version in ["18"]:
        
        steps = [
            ('preprocessor', preprocessor),
            ('pca', PCA(random_state=42))
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
    elif type_model == "gnb":
        steps.append(
            ('gnb', GaussianNB())
        )
    else:
        raise NotImplementedError
        
    pipeline = Pipeline(steps=steps)
    
    return pipeline