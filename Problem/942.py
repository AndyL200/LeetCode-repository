def diStringMatch(self, s: str) -> List[int]:
        n = len(s)
        p = deque()
        for i in range(n+1):
            p.append(i)
        res = []
        for c in s:
            if c == 'I':
                res.append(p.popleft())
            else:
                res.append(p.pop())

        res.append(p.pop())
        return res