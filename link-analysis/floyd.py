def floyd(mat):
    x = len(mat)
    y = len(mat[0])
    SP = preprocess(mat)
    if x == y:
        for k in range(x):
            for i in range(x):
                for j in range(x):
                    SP[i,j]=min((SP[i,k]+SP[k,j],SP[i,j]))
    else:
        print('error')
    for i in range(x):
        SP[i,i]=0
    return SP
