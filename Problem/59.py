def generateMatrix(n: int):
    op = 0
    i = 0
    j = 0
    a = 1
    t = n**2
    visited = set()
    res = [[0] * n for _ in range(n)]
    while a < t:
        if op == 0:
            while i < n-1 and (j*n+i+1) not in visited:
                visited.add(j*n+i)
                res[j][i] = a
                a += 1
                i += 1
            op = 1
        elif op == 1:
            while j < n-1 and ((j+1)*n+i) not in visited:
                visited.add(j*n+i)
                res[j][i] = a
                a += 1
                j += 1
            op = 2
        elif op == 2:
            while i > 0 and (j*n+i-1) not in visited:
                visited.add(j*n+i)
                res[j][i] = a
                a += 1
                i-=1
            op = 3
        else:
            while j > 0 and ((j-1)*n+i) not in visited:
                visited.add(j*n+i)
                res[j][i] = a
                a += 1
                j -= 1
                
            op = 0
    res[j][i] = a
    return res


print(generateMatrix(3))