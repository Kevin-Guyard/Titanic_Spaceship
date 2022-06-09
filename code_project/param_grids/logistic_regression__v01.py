param_grid_logistic_regression__v01 = [
    {
        "logistic__solver": ["liblinear"],
        "logistic__penalty": ["l1", "l2"],
        "logistic__C": list(np.logspace(-5, 5, 31)),
    },
    {
        "logistic__solver": ["saga"],
        "logistic__penalty": ["elasticnet"],
        "logistic__C": list(np.logspace(-5, 5, 31)),
        "logistic__l1_ratio": list(np.linspace(0.1, 0.9, 9)),
    }
]