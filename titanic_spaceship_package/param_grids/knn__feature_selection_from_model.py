import numpy as np

param_grid_knn__feature_selection_from_model = {
    "knn__n_neighbors": list(map(int, np.linspace(1, 150, 150))),
    "knn__weights": ["uniform", "distance"],
    "knn__p": [1, 2],
    "feature_selection__max_features": list(map(int, np.linspace(1, 27, 27))),
}