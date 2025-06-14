# def longestIncreasingPath(matrix) -> int:
#     directions = [(1,0), (-1,0), (0,1), (0,-1)]

#     def dfs(r, c, acc, visited):
#         nonlocal directions
#         m = acc
#         for d in directions:
#             x, y = d
#             if 0 <= (r + x) < len(matrix) and 0 <= (c + y) < len(matrix[r]):
#                 if matrix[r+x][c+y] > matrix[r][c] and (len(matrix)*(r+x)+c+y) not in visited:
#                     visited.add(len(matrix)*(r+x)+(c+y))
#                     m+=1
#                     acc = max(acc, dfs(r + x, c + y, m, visited))
#                     m-=1
#                     visited.remove(len(matrix)*(r+x)+(c+y))
#         return acc


#     great = 0

#     for r in range(len(matrix)):
#         for c in range(len(matrix[r])):
#             visited = set()
#             visited.add(len(matrix)*r+c)
#             doc = dfs(r, c, 1, visited)
#             if doc > great:
#                 great = doc
#     return great


def longestIncreasingPath(matrix) -> int:
    directions = [(-1,0), (0,-1)]
    m = len(matrix)
    n = len(matrix[0])

    dp = [[0] * n for _ in range(m)]
    dp[m-1][n-1] = 1
    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):
            for d in directions:
                x, y = d
                if 0 <= (i + x) < m and 0 <= (j + y) < n:
                    if matrix[i+x][j+y] > matrix[i][j]:
                        dp[i+x][j+y] = max(dp[i][j]+1, dp[i+x][j+y])
                    elif dp[i+x][j+y] == 0:
                        dp[i+x][j+y] = 1
    return dp[0][0]

print(longestIncreasingPath(matrix = [[9,9,4],[6,6,8],[2,1,1]]))