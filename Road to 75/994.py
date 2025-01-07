def orangesRotting(self, grid):
        
        m = len(grid)
        n = len(grid[0])

        directions = [(1,0),(0,1),(-1,0),(0,-1)]


        q = deque()
        fresh = 0
        for y in range(len(grid)):
            for x in range(len(grid[y])):
                if grid[y][x] == 2:
                    grid[y][x] = 3
                    q.append((y,x))
                elif grid[y][x] == 1:
                    fresh+=1
        


        if fresh == 0:
            return 0
        if not q:
            return -1
        minutes = 0


        while q and fresh > 0:
            
            minutes += 1
            for i in range(len(q)):
                r, c = q.popleft()

            
                for dr, dc in directions:
                    r0 = r + dr
                    c0 = c + dc
                    
                    if 0<=r0<m and 0<=c0<n and grid[r0][c0] == 1:
                        q.append((r0,c0))
                        grid[r0][c0] = 2
                        fresh-=1

           

        if fresh > 0:
            return -1
        else:
            return minutes
