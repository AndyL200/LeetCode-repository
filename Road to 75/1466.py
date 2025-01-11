def dfs(self, matrix, visited, node):
    change = 0
    visited[node] = True
    for i in matrix[node]:
        if not visited[abs(i)]:
            change += self.dfs(matrix, visited, abs(i)) + (1 if i > 0 else 0)

    return change
def minReorder(self, n: int, connections: List[List[int]]) -> int:
    visited = [False] * n
    matrix = [[] for _ in range(n)]

    for c in connections:
        matrix[c[0]].append(c[1])
        matrix[c[1]].append(-c[0])
    return self.dfs(matrix, visited, 0)