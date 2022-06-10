from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import FunctionTransformer
from sklearn.preprocessing import PowerTransformer
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
import numpy as np

features_1 = ["RoomService", "FoodCourt", "ShoppingMall", "Spa", "VRDeck"]
features_2 = ["Age"]
features_3 = ["CryoSleep", "VIP"]
features_4 = ["HomePlanet", "Destination", "CabinDeck", "CabinSide"]

transformer_1 = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value=0)),
    ('log', FunctionTransformer(func=lambda x: np.log(x+1))),
    ('scaler', StandardScaler()),
])

transformer_2 = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='mean')),
    ('yeo_jonhson', PowerTransformer(method='yeo-johnson', standardize=True)),
])

transformer_3 = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value=False)),
    ('caster', FunctionTransformer(func=lambda x: np.int64(x))),
])

transformer_4 = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='Unknown')),
    ('encoder', OneHotEncoder(handle_unknown='ignore', sparse=False)),
])

preprocessor = ColumnTransformer(transformers=[
    ('features_1', transformer_1, features_1),
    ('features_2', transformer_2, features_2),
    ('features_3', transformer_3, features_3),
    ('features_4', transformer_4, features_4),
])