def largestMagicSquare(grid) -> int:
    m = len(grid)
    n = len(grid[0])
    def is_magic(i, j, k):
        target = sum(grid[i][j:j+k])

        for r in range(i, i+k):
            row = sum(grid[r][j:j+k])
            if row != target:
                return False
        
        for c in range(j, j+k):
            col = 0
            for r in range(i, i+k):
                col += grid[r][c]
            if col != target:
                return False
        diag = 0    
        for t in range(k):
            diag += grid[i+t][j+t]
        if diag != target:
            return False
        diag_r = 0
        for t in range(k):
            diag_r += grid[i+t][j+(k-1-t)]
        return diag_r == target
    
    for k in range(min(m, n), 0, -1):
        for i in range(0, m-k+1):
            for j in range(0, n-k+1):
                if is_magic(i,j,k):
                    return k
    return 1

print(largestMagicSquare([[7,1,4,5,6],[2,5,1,6,4],[1,5,4,3,2],[1,2,7,3,4]]))