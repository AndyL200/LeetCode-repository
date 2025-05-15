def solveSudoku(board):
        
    rows = [0] * 9
    cols = [0] * 9
    boxes = [0] * 9
    empty = []

    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                empty.append((i,j))
            else:
                n = int(board[i][j])
                bit = 1 << (n-1)
                rows[i] |= bit
                cols[j] |= bit
                boxes[(i//3) * 3 + (j//3)] |= bit


    def dfs(k):
        if k == len(empty):
            return True
        i, j = empty[k]
        b = (i // 3) * 3 + (j // 3)
        mask = ~(rows[i] | cols[j] | boxes[b]) & ((1 << 9) - 1)
        while mask:
            bit = mask & -mask
            n = bit.bit_length()
            board[i][j] = str(n)
            rows[i] |= bit
            cols[j] |= bit
            boxes[b] |= bit
            if dfs(k + 1):
                return True
            board[i][j] = '.'
            rows[i] ^= bit
            cols[j] ^= bit
            boxes[b] ^= bit
            mask &= mask-1
        return False
    dfs(0)