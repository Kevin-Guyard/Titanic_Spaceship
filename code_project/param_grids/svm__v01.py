param_grid_svm__01 = [
    {
        "svm__C": list(np.logspace(-5, 5, 1)), 
        "svm__kernel": ["linear", "rbf", "sigmoid"]
    },
    {
        "svm__C":  list(np.logspace(-5, 5, 1)),
        "svm__kernel": ["poly"],
        "svm__degree": list(map(int, np.linspace(1, 5, 1)))
    }
]