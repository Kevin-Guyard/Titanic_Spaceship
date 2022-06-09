param_grid_knn__v01 = {
    "knn__n_neighbors": list(map(int, np.linspace(1, 10, 10))),
    "knn__weights": ["uniform", "distance"],
    "knn__p": [1, 2]
}