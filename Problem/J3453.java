import java.util.*;   
class J3453 { 
    public double separateSquares(int[][] squares) {
        double max_y = 0;
        double total_area = 0;
        for(int[] sq : squares) {
            int y = sq[1];
            int l = sq[2];
            total_area += (double) l*l;
            max_y = Math.max(max_y, (double) (y+l));
        }

        double low = 0;
        double high = max_y;
        double prec = 1e-5;
        while(Math.abs(high-low) > prec) {
            double mid = (high + low)/2.0;
            double area = calculateArea(squares, mid);
            if (area * 2 >= total_area) {
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
        for(int[] sq : squares) {
            int y = sq[1];
            int l = sq[2];

            area += (double) l * Math.max(0, Math.min(curY-y, l));
        }
        
        return area;
    }

    public static void main(String[] args) {
        J3453 solution = new J3453();
        System.out.println(solution.separateSquares(new int[][]{{0,0,1},{2,2,1}}));
    }
}
    
