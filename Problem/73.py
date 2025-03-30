def setZeroes(matrix) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    m = len(matrix)
    n = len(matrix[0])

    first_r = False
    first_c = False
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:

                matrix[0][j] = 0
                matrix[i][0] = 0

                if i == 0:
                    first_r = True
                    if j == 0:
                        first_c = True
    

    for i in range(1,m):
        for j in range(1,n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    if first_c:
        for i in range(m):
            matrix[i][0] = 0
    if first_r:
        for j in range(n):
            matrix[0][j] = 0

print(setZeroes([[1,0,3]]))