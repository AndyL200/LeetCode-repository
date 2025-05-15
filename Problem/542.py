def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        m = len(mat)
        n = len(mat[0])
        INF = 10 ** 20
                
        res = [[INF] * n for _ in range(m)]

        q = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    res[i][j] = 0
                    q.append((i,j))
        acc = 0
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and res[nx][ny] == INF:
                    res[nx][ny] = res[x][y] + 1
                    q.append((nx,ny))
        return res