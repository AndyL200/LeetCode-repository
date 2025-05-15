from collections import deque
def solveSudoku(board):
    """
    Do not return anything, modify board in-place instead.
    """

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '.':
                board[i][j] = 0
            else:
                board[i][j] = int(board[i][j])

    def oRow(i, j, n):
        t1 = i % 3
        t2 = t1
        while t1 < 3:
            if (rows[t1] & (1 << (n-1))) <= 0 and board[t1][j] == 0:
                return False
            t1+=1
        while t2 >= 0:
            if (rows[t2] & (1 << (n-1))) <= 0 and board[t2][j] == 0:
                return False
            t2-=1
        
        return True

    def oCol(i, j ,n):
        t1 = j % 3
        t2 = t1
        while t1 < 3:
            if (cols[t1] & (1 << (n-1))) <= 0 and board[i][t1] == 0:
                return False
            t1+=1
        while t2 >= 0:
            if (cols[t2] & (1 << (n-1))) <= 0 and board[i][t2] == 0:
                return False
            t2-=1
        
        return True

    def singleSetBit(n):
        return n > 0 and (n & (n - 1)) == 0

    
    q = deque()
    
    rows = []
    cols = []
    boxes = []


    for i in range(len(board)):
        r = 0
        c = 0
        b = 0

        for j in range(len(board)):
            if board[i][j] != 0:
                r ^= (1 << (board[i][j] - 1))
            else:
                q.append((i,j))
            if board[j][i] != 0:
                c ^= (1 << (board[j][i] - 1))
            if board[(i-i%3)+j//3][(i%3*3+j%3)] != 0:
                b ^= (1 << (board[(i-i%3)+j//3][(i%3*3+j%3)] - 1 ))
        rows.append(r)
        cols.append(c)
        boxes.append(b)
    
    while q:
        y, x = q.popleft()
        bi = (y//3) * 3 + (x//3)
        poss = (~(rows[y] | cols[x] | boxes[bi])) & ((1 << 9) - 1)


        print(f"rows[{y}]: {bin(rows[y])}, cols[{x}]: {bin(cols[x])}, boxes[{bi}]: {bin(boxes[bi])}")
        print(f"Computed poss: {bin(poss)} ({poss})")

        if singleSetBit(poss):
            board[y][x] = (poss & -poss).bit_length()
            rows[y] |= (1 << (board[y][x] - 1))
            cols[x] |= (1 << (board[y][x] - 1))
            boxes[bi] |= (1 << (board[y][x] - 1))

        else:
            while poss > 0:
                s = (poss & -poss).bit_length()

                if oRow(y, x, s) and oCol(y, x, s):
                    board[y][x] = s
                    rows[y] |= (1 << (board[y][x] - 1))
                    cols[x] |= (1 << (board[y][x] - 1))
                    boxes[bi] |= (1 << (board[y][x] - 1))
                    break

                poss &= poss - 1


        if board[y][x] == 0:
            q.append((y,x))

    return board


print(solveSudoku([[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]))