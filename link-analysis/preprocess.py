def preprocess(mat):
    x = len(mat)
    y = len(mat[0])
    for i in range(x):
        for j in range(y):
            if mat[i, j] == 0:
                mat[i, j] = 100000
    return mat

