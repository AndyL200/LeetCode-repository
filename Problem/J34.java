
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
        int i = 1, r = 0, l = 0;
        while(index - i > -1 && nums[index-i] == nums[index]) {
            l++;
            i++;
        }
        i = 1;
        while(index + i < nums.length && nums[index+i] == nums[index]) { 
            r++;
            i++;
        }
        return new int[] {index-l, index+r};
    }

    public static void main(String[] args) {
        J34 hire = new J34();
        System.out.println(Arrays.toString(hire.searchRange(new int[] {1,2,3}, 1)));
    }
}