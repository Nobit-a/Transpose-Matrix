import numpy as np
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
trans = np.zeros((len(mat[0]), len(mat)))

for i in range(len(mat)):
    for j in range(len(mat[0])):
        trans[i][j] = mat[j][i]

print(trans)
