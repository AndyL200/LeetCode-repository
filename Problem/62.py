def uniquePaths(m: int, n: int) -> int:
        grid = []
        for _ in range(m-1):
            base_row = [0]*(n-1)
            base_row.append(1)
            grid.append(base_row)
        fin_row = [1] * n
        grid.append(fin_row)

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                t1 = grid[i+1][j]
                t2 = grid[i][j+1] 
                tmp = t1 + t2
                print(tmp)
                grid[i][j] = tmp

        return grid[0][0]

print(uniquePaths(2,7))
