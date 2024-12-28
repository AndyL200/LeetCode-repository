
import java.util.Arrays;

public class J2352 {

    public static int equalPairs(int[][] grid) {
        int matches = 0;
        int n = grid.length;
        int cols[][] = new int[n][n];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cols[i][j] = grid[j][i];
            }

        }

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (Arrays.equals(grid[i], cols[j])) {
                    matches++;
                }
            }

        }

        return matches;
    }

    public static void main(String args[]) {
        int[][] grid = {{3, 2, 1}, {1, 7, 6}, {2, 7, 7}};
        System.out.print(equalPairs(grid));
    }
}
