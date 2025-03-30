def combine(n: int, k: int):
    res = []
    combo = []
    
    def dfs(start):
        if len(combo) == k:
            res.append(combo.copy())
            return
        for i in range(start, n+1):
            combo.append(i)
            dfs(i+1)
            combo.pop()
    dfs(1)
    return res