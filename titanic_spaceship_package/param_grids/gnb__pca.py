import numpy as np

param_grid_gnb__pca = {
    "gnb__var_smoothing": np.logspace(-9, 0, 100),
    "pca__n_components": list(map(int, np.linspace(1, 28, 28)))
}