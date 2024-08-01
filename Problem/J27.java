public class J27 {
    public int removeElement(int[] nums, int val) {
        int count = 0;
        int countBad = 0;
        for(int i = 0; i < nums.length-countBad; i++) {
            if(nums[i] == val) {
                countBad++;
                for(int j = i; j < nums.length-1; j++) {
                    int temp = nums[j];
                    nums[j] = nums[j+1];
                    nums[j+1] = temp;
                    
                }
                i--;
            }
            else {
                count++;
            }
        }
        return count;
    }
    public static void main(String args[]) {
        J27 hire = new J27();
        int[] x = {0,1,2,2,3,0,4,2};
        System.out.print(hire.removeElement(x,2));
    }
}
