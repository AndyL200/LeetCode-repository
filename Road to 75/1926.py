def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m = len(maze)
        n = len(maze[0])

        

        for r in range(m):
            if maze[r][0] == '.':
                maze[r][0] = 'e'
            if maze[r][-1] == '.':
                maze[r][-1] = 'e'
        for col in range(n):
            if maze[0][col] == '.':
                maze[0][col] = 'e'
            if maze[-1][col] == '.':
                maze[-1][col] = 'e'



        r, col = entrance

        maze[r][col] = 's'
        
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        visited = [[False] * n for _ in range(m)]
        visited[r][col] = True
        q = deque()
        q.append((r,col))
        res = 1
        while q:
            for i in range(len(q)):
                row, c = q.popleft()
                for dr, dc in directions:
                    r0, c0 = row + dr, c + dc
                    if 0 <= r0 < m and 0 <= c0 < n and not maze[r0][c0] == '+':
                        if not visited[r0][c0]:
                            q.append((r0,c0))
                            visited[r0][c0] = True
                            if maze[r0][c0] == 'e':
                                return res
                
            res += 1

        return -1


