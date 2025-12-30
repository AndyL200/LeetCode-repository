def numSquares(self, n: int) -> int:
    v = 1
    li = []
    while (v*v <= n):
        li.append(v*v)
        v += 1
    q = [n]
    visited = set()
    visited.add(n)
    level = 0
    while q:
        level += 1
        for _ in range(len(q)):
            cur = q.pop(0)
            for s in li:
                nxt = cur - s
                if nxt == 0:
                    return level
                if nxt < 0:
                    break
                if nxt not in visited:
                    visited.add(nxt)
                    q.append(nxt)
    return 0