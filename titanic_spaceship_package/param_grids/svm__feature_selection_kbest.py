import numpy as np

param_grid_svm__feature_selection_kbest = [
    {
        "svm__C": list(np.logspace(-2, 2, 13)), 
        "svm__kernel": ["linear", "rbf", "sigmoid"],
        "feature_selection__k": list(map(int, np.linspace(1, 27, 27))),
    },
    {
        "svm__C": list(np.logspace(-2, 2, 13)), 
        "svm__kernel": ["poly"],
        "svm__degree": list(map(int, np.linspace(1, 5, 5))),
        "feature_selection__k": list(map(int, np.linspace(1, 27, 27))),
    }
]