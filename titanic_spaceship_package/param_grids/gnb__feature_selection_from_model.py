import numpy as np

param_grid_gnb__feature_selection_from_model = {
    "gnb__var_smoothing": np.logspace(-9, 0, 100),
    "feature_selection__max_features": list(map(int, np.linspace(1, 27, 27))),
}