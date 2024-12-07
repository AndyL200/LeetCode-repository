
import java.util.Arrays;

class J34 {

    public int binarySearch(int nums[], int target) {
        if(nums.length <= 0) { return -1;}
        int left = 0, right = nums.length-1;
        int mid = (left+right)/2;
        if(target == nums[mid]) {
            return mid;
        }
        else if(target > nums[mid]) {
            return binarySearch(nums, mid + 1, right, target);
        }
        else {
            return binarySearch(nums, left, mid-1, target);
        }
    }
    public int binarySearch(int n[], int left, int right, int target) {

        int mid = (left+right)/2;
        if(left > right) {
            return -1;
        }
        if(target == n[mid]) {
            return mid;
        }
        else if(target > n[mid]) {
            return binarySearch(n, mid + 1, right, target);
        }
        else {
            return binarySearch(n, left, mid-1, target);
        }
    }


    public int[] searchRange(int[] nums, int target) {
        int index = binarySearch(nums, target);

        if(index == -1) {return new int[] {-1,-1};}

        int r = index, l = index;
        int i;
        if(index > 0) {

            i = binarySearch(nums, 0, index-1, target); 

            while(i != -1) {
                l = i;
                i = binarySearch(nums, 0, i-1, target); 
            }
        }

        if(index < nums.length-1) {

            i = binarySearch(nums, index+1, nums.length-1,  target);

            while(i != -1) { 
                r = i;
                i = binarySearch(nums, i+1, nums.length-1,  target); 
            }
        }
       
       
        return new int[] {l, r};
    }

    public static void main(String[] args) {
        J34 hire = new J34();
        System.out.println(Arrays.toString(hire.searchRange(new int[] {1,2,3,3,3,3,4,5,9}, 3)));
    }
}