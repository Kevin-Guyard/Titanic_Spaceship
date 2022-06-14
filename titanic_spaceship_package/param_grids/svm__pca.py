import numpy as np

param_grid_svm__pca = [
    {
        "svm__C": list(np.logspace(-2, 2, 13)), 
        "svm__kernel": ["linear", "rbf", "sigmoid"],
        "pca__n_components": list(map(int, np.linspace(1, 28, 28)))
    },
    {
        "svm__C": list(np.logspace(-2, 2, 13)), 
        "svm__kernel": ["poly"],
        "svm__degree": list(map(int, np.linspace(1, 5, 5))),
        "pca__n_components": list(map(int, np.linspace(1, 28, 28)))
    }
]