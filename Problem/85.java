
class Solution {

    public int expand(char[][] matrix, int i, int j) {
        int maxArea = 0;
        int rows = matrix.length;
        int cols = matrix[0].length;
        int minWidth = cols;

        for (int y = i; y < rows; y++) {
            if (matrix[y][j] == '0') {
                break;
            }
            int width = 0;
            for (int x = j; x < cols; x++) {
                if (matrix[y][x] == '1') {
                    width++;
                } else {
                    break;
                }
            }
            minWidth = Math.min(minWidth, width);
            int height = y - i + 1;
            int area = minWidth * height;
            maxArea = Math.max(maxArea, area);
        }
        return maxArea;
    }
    public int maximalRectangle(char[][] matrix) {
        if (matrix == null || matrix.length == 0 || matrix[0].length == 0) {
            return 0;
        }
        int maxArea = 0;
        int rows = matrix.length;
        int cols = matrix[0].length;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
               maxArea = Math.max(maxArea, expand(matrix, i, j));
            }
        }
        return maxArea;    
    }

    public static void main(String[] args) {
        
    }
}
