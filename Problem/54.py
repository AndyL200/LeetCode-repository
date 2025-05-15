
def spiralOrder(matrix):
    directions = [(1,0), (0,1), (-1,0), (0,-1)]

    d = 0
    x = -1
    y = 0
    m = len(matrix)
    n = len(matrix[0])
    spin = [n, m-1]
    res = []
    while spin[d % 2] != 0:
        for _ in range(spin[d%2]):
            x += directions[d][0]
            y += directions[d][1]
            res.append(matrix[y][x])
        spin[d%2] -= 1
        d = (d+1) % 4
    return res