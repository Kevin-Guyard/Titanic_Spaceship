import numpy as np

param_grid_knn__v02 = {
    "knn__n_neighbors": list(map(int, np.linspace(1, 300, 300))),
    "knn__weights": ["uniform", "distance"],
    "knn__p": [1, 2],
    "feature_selection__k": list(map(int, np.linspace(1, 27, 27))),
}