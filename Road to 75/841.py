def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
    n = len(rooms)
    visited = [False] * n
    visited[0] = True
    q = [rooms[0]]
    s = 0
    fin = (n)/2* (n-1)
    while q:
        for i in range(len(q)):
            curr = q.pop(0)
            for j in curr:
                if not visited[j]:
                    s += j
                    visited[j] = True
                    q.append(rooms[j])
        if s == fin:
            return True
        
    return False

#beats 100% using natural numbers