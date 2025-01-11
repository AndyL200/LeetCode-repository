def dfs(self, node, isConnected, visited):
    visited[node] = True
    for i in range(len(isConnected)):
        if isConnected[node][i] and not visited[i]:
            self.dfs(i, isConnected, visited)

def findCircleNum(self, isConnected: List[List[int]]) -> int:
    n = len(isConnected)
    provinces = 0
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            provinces += 1
            self.dfs(i, isConnected, visited)
        
    return provinces
