class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1 and not word2:
            return 0
        elif not word1:
            return len(word2)
        elif not word2:
            return len(word1)
        m = len(word1)
        n = len(word2)
        grid = [[float('inf')] * (n+1) for _ in range(m+1)]
        i = n
        while i > 0:
            grid[m][i] = n-i
            i-=1
        i = m
        while i > 0:
            grid[i][n] = m-i
            i-=1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if word1[i] == word2[j]:
                    grid[i][j] = grid[i+1][j+1]
                else:
                    grid[i][j] = 1 + min(grid[i+1][j+1], grid[i+1][j], grid[i][j+1])

        return grid[0][0]