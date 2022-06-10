import numpy as np

param_grid_svm__v01 = [
    {
        "svm__C": list(np.logspace(-4, 4, 17)), 
        "svm__kernel": ["linear", "rbf", "sigmoid"]
    },
    {
        "svm__C":  list(np.logspace(-4, 4, 17)),
        "svm__kernel": ["poly"],
        "svm__degree": list(map(int, np.linspace(1, 3, 3)))
    }
]