import numpy as np

param_grid_logistic_regression__pca = [
    {
        "logistic__solver": ["liblinear"],
        "logistic__penalty": ["l1", "l2"],
        "logistic__C": list(np.logspace(-5, 5, 31)),
        "pca__n_components": list(map(int, np.linspace(1, 28, 28)))
    },
    {
        "logistic__solver": ["saga"],
        "logistic__penalty": ["elasticnet"],
        "logistic__C": list(np.logspace(-5, 5, 31)),
        "logistic__l1_ratio": list(np.linspace(0.1, 0.9, 9)),
        "pca__n_components": list(map(int, np.linspace(1, 28, 28)))
    }
]