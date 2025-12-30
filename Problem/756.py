def pyramidTransition(self, bottom: str, allowed: List[str]) -> bool:
    n = len(bottom)

    lookup = collections.defaultdict(list)

    for s in allowed:
        x, y, z = list(s)
        lookup[x + y].append(z)

    levels = [list(bottom)]

    while len(levels) < n:
        levels.append([""] * (len(levels[-1]) - 1))

    def go(level, col):
        if level == n:
            return True
        elif col >= len(levels[level]):
            return go(level+1, 0)
        current = levels[level-1][col] + levels[level-1][col+1]

        for c in lookup[current]:
            levels[level][col] = c
            if go(level, col+1):
                return True
            levels[level][col] = ""
        return False
    
    return go(1,0)