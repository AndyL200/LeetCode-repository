public class Solution {

    //make a binary search

    public int binarySearch(int[] nums, int val, int startingIndex = 0) {
        int high, low, mid;
        high = nums.Length-1;
        low = startingIndex;
        mid = (high + low)/2;
    while(low != high) {
        if(nums[mid] > val) {
            high = mid;
            mid = (high + low)/2;
        }
        else if (nums[mid] < val) {
            low = mid;
            mid = (high + low)/2;

        }
        else if(nums[mid] == val) {return mid;}

    }
    return -1;
    }
    public int RemoveDuplicates(int[] nums) {
        int badCount = 0;
        for(int i = 0; i < nums.Length; i++) {
            if(binarySearch(nums,nums[i],i) == -1) {
                badCount += 1;
                for(int t = i; t < nums.Length-1; t++) {
                    int temp = nums[i];
                    nums[i] = nums[i+1];
                    nums[i+1] = temp;
                }
            }
        }
        return nums.Length - badCount;
    }
    void main() {}
}