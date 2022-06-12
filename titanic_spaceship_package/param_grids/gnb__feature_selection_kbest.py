import numpy as np

param_grid_gnb__feature_selection_kbest = {
    "gnb__var_smoothing": np.logspace(-9, 0, 100),
    "feature_selection__k": list(map(int, np.linspace(1, 27, 27))),
}