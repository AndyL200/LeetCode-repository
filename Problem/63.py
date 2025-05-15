def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        matrix = [[1]*n for _ in range(m)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i+1 < m and j+1 < n:
                    matrix[i][j] = matrix[i+1][j] + matrix[i][j+1]
                elif j+1 < n:
                    matrix[i][j] = matrix[i][j+1]
                elif i+1<m:
                    matrix[i][j] = matrix[i+1][j]
                if obstacleGrid[i][j] == 1:
                    matrix[i][j] = 0

        return matrix[0][0]

