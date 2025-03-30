def totalNQueens(self, n: int) -> int:
    cols = set()
    posDiag = set()
    negDiag = set()
    total = 0

    def backtrack(r):
        nonlocal total
        if r >= n:
            total += 1
            return
        
        for i in range(n):
            if i not in cols and r+i not in posDiag and r-i not in negDiag:
                cols.add(i)
                posDiag.add(r+i)
                negDiag.add(r-i)

                backtrack(r+1)

                cols.remove(i)
                posDiag.remove(r+i)
                negDiag.remove(r-i)
    backtrack(0)
    return total