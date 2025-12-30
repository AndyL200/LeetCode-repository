def numMagicSquaresInside(grid) -> int:
    count = 0
    
    def expand3by3(r, c):

        
        if grid[r+1][c+1] != 5:
            return False
        
        vals = [grid[r+i][c+j] for i in range(3) for j in range(3)]

        if sorted(vals) != list(range(1,10)):
            return False
        
        #Rows
        if sum(grid[r][c:c+3]) != 15:
            return False
        if sum(grid[r+1][c:c+3]) != 15:
            return False
        if sum(grid[r+2][c:c+3]) != 15:
            return False
        #Columns
        if grid[r][c] + grid[r+1][c] + grid[r+2][c] != 15:
            return False
        if grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] != 15:
            return False
        if grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] != 15:
            return False
        #Diagonals
        if grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] != 15: return False
        if grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] != 15: return False

        return True

    for i in range(len(grid)-2):
        for j in range(len(grid[i])-2):
            if expand3by3(i,j):
                count += 1

    return count


print(numMagicSquaresInside([[4,3,8,4],
                             [9,5,1,9], 
                             [2,7,6,2]]))  # 1