public class J45 {
    public int jump(int[] nums) {
        //using a sliding window
        int l, r;
        int jumps = 0;
        l=r=0;
        while(r < nums.length-1) {
         int farthest = 0;
         for(int i = l; i < r+1; i++) {
             farthest = Math.max(farthest, i + nums[i]);
         }
         l = r + 1;
         r = farthest;
         jumps++;
        }
        return jumps;
 
    
     }   

    public void main(String args[]) {
        J45 hire = new J45();
        int x[] = {1,2,3,4,5,6,7,4,5,6,8,9,0};
        System.out.print(hire.jump(x));
    }
}
