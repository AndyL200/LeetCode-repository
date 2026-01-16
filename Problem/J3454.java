import java.util.Arrays;
import java.util.Comparator;

public class J3454 {
    class compareY implements Comparator<int[]> {
        public int compare(int[] a, int[] b) {
            return Integer.compare(a[1], b[1]);
        }
    }
    public double separateSquares(int[][] squares) {
        double totalArea = 0;
        double max_y = 0, min_y = 0;
        Arrays.sort(squares, new compareY());
        for(int[] sq : squares) {
            int l = sq[2];
            int y = sq[1];
            totalArea += (double)l*l;
            min_y = Math.min(min_y, y);
            max_y = Math.max(max_y, y+l);
        }

        double low = min_y;
        double high = max_y;
        while (Math.abs(high-low) > 1e-5) {
            double mid = (high + low)/2.0;
            double area = calculateArea(squares, mid);
            if (area * 2 >= totalArea) {
                high = mid;
            }
            else {
                low = mid;
            }
        }
            return high;
    }

    private double calculateArea(int[][] squares, double curY) {
        double area = 0;
        double prevTop = 0;
        for(int i = 0; i < squares.length; i++) {
            int x = squares[i][0];
            int y = squares[i][1];
            int l = squares[i][2];
            if (y < prevTop) {
                double overlap_x = (squares[i-1][0] + squares[i-1][2] - x);
                double overlap_y = (curY < prevTop && curY > y)? (prevTop - y) : (prevTop-curY);
                area += (double) l * Math.max(0, Math.min(curY-y, l)) - (overlap_x*overlap_y);
            }
            else {
                area += (double) l * Math.max(0, Math.min(curY-y, l));
            }
            prevTop = (double) y + l;
        }
        return area;
    }

    public static void main(String[] args) {
        J3454 solution = new J3454();
        System.out.println(solution.separateSquares(new int[][]{{0,0,1},{2,2,1}}));
    }
}
