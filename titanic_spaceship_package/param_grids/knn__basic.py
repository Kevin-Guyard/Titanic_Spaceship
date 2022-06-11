import numpy as np

param_grid_knn__basic = {
    "knn__n_neighbors": list(map(int, np.linspace(1, 500, 500))),
    "knn__weights": ["uniform", "distance"],
    "knn__p": [1, 2]
}