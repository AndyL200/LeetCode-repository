public class J1493alt {
    public int longestSubarray(int[] nums) {
        int lastTotal = 0;
        int runningTotal = 0;
        int max = 0;
        for(int i = 0; i < nums.length-1; i++) {
            if(nums[i] == 1) {runningTotal++;}
            else {lastTotal = runningTotal; runningTotal = 0;}
            if(max < lastTotal + runningTotal) {max = lastTotal + runningTotal;}
        }
        return max;
    }
    public static void main(String args[]) {
        int[] x = {1,1,0,0,1,1};
        J1493alt h = new J1493alt();
        System.out.println(h.longestSubarray(x));
    }
}
