import java.util.HashSet;

public class J36 {


public boolean isValidSudoku(char[][] board) {
    for(int y = 0; y < board.length; y++) {
        HashSet<Character> rowCheck = new HashSet<Character>();
        for(int x = 0; x < board[y].length;x++) {
            if(board[y][x] != '.' && rowCheck.contains(board[y][x])) {
                return false;
            }
            else {
                rowCheck.add(board[y][x]);
            }
            if((x+1)%3 == 0 && (y+1)%3 == 0) {
                int i = 3;
                HashSet<Character> threebythree = new HashSet<Character>();
                while(i > 0) {
                    int j = 3;
                    while(j > 0) {
                        if(board[y+1-i][x+1-j] != '.' && threebythree.contains(board[y+1-i][x+1-j])) {
                            return false;
                        }
                        else {
                            threebythree.add(board[y+1-i][x+1-j]);
                        }
                        j--;
                    }
                    i--;
                }
            }   
        }
    }
    for(int x = 0; x < board[0].length; x++) {
        HashSet<Character> colCheck = new HashSet<Character>();
        for(int y = 0; y < board.length; y++) {
            if(board[y][x] != '.' && colCheck.contains(board[y][x])) {
                return false;
            }
            else {
                colCheck.add(board[y][x]);
            }
        }
    }
    
    return true;
}

static public void main(String args[]) {
    J36 hire = new J36();
    char[][] c = {
     {'5','3','.','.','7','.','.','.','.'},
     {'6','.','.','1','9','5','.','.','.'}
    ,{'.','9','8','.','.','.','.','6','.'}
    ,{'8','.','.','.','6','.','.','.','3'}
    ,{'4','.','.','8','.','3','.','.','1'}
    ,{'7','.','.','.','2','.','.','.','6'}
    ,{'.','6','.','.','.','.','2','8','.'}
    ,{'.','.','.','4','1','9','.','.','5'}
    ,{'.','.','.','.','8','.','.','7','9'}
};
    System.out.println(hire.isValidSudoku(c));
}
}