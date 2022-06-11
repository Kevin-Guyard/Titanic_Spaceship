import numpy as np

param_grid_svm__basic = [
    {
        "svm__C": list(np.logspace(-2, 2, 13)), 
        "svm__kernel": ["linear", "rbf", "sigmoid"]
    },
    {
        "svm__C": list(np.logspace(-2, 2, 13)), 
        "svm__kernel": ["poly"],
        "svm__degree": list(map(int, np.linspace(1, 5, 5)))
    }
]