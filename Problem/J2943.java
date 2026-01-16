import java.util.*;

public class J2943 {
    public int maximizeSquareHoleArea(int n, int m, int[] hBars, int[] vBars) {
        int x = find(hBars), y = find(vBars);
        int res = Math.min(x, y) + 1;
        return res * res;
    }
    private int find(int[] arr) {
        Arrays.sort(arr);
        int area = 1;
        int i = 0;
        int n = arr.length;
        
        while(i < n) {
            int count = 1;
            while(i+1 < n && arr[i]+1 == arr[i+1]) {
                i+=1;
                count+=1;
            }
            i+=1;
            area = Math.max(area, count);
        }
        return area;
    }
}
