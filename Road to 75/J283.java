public class J283 {
    //
    public void moveZeroes(int[] nums) {
        int i = 0;
            while(nums[i] != 0 || i == nums.length) {
                i++;
            }
            while(i < nums.length-1) {
                int j = i;
                    while(j < nums.length-1 && nums[j] == 0) {j++;}
                    int range = j-i;
                    for(int z = 0; z < range;z++) {
                    int temp = nums[i];
                    nums[i] = nums[j];
                    nums[j] = temp;
                    i++;
                    j++;
                    }
            }
            }
    public static void main(String args[]) {
        J283 hire = new J283();
        int[] x = {0,1,0,3,12};
        hire.moveZeroes(x);
        for(int i: x) {
            System.out.println(i);
        }
    }
}
