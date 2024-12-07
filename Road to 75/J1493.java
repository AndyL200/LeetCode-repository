public class J1493 {
    public int longestSubarray(int[] nums) {
        int max = 0;
        int range = nums.length;

        int b[] = new int[range];
        int count = 0;

        for(int i = 0; i < range; i++) {
            if(nums[i] != 1) {b[count] = i; count++;}
        }
        if(count == 0) {max = range-1;}

        for(int k = 0; k < count; k++) {
            boolean left = (k-1 >= 0), right  = (k+1 < count);
            if(left && right) { 
                int curMax = b[k+1]-b[k-1]-2;
                if(max < curMax) {max = curMax;}
            }
            else if(left) {
                int curMax = Math.max(b[k]-b[k-1]-1,range-b[k-1]-1);
                if(max < curMax) {max = curMax;}

            }
            else if(right) {
                int curMax  = Math.max(b[k+1]-1,b[k+1]-b[k]-1);
                if(max < curMax) {max = curMax;}

            }
            else {
                max = range-1; break;
            }
        }
    return max;
    }
    public static void main(String args[]) {
        int[] x = {1,1,0,0,1,1};
        J1493 h = new J1493();
        System.out.println(h.longestSubarray(x));
    }
}
