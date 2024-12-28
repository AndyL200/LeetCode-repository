
public class J334 {

    //naive
    static public boolean increasing(int[] nums) {
        int n = nums.length;
        int min = nums[0], max = nums[n - 1];
        int[] pre = new int[n];
        int[] post = new int[n];
        for (int i = 0; i < n; i++) {
            if (nums[i] < min) {
                min = nums[i];
            }
            pre[i] = min;
        }
        for (int i = n - 1; i >= 0; i--) {
            if (nums[i] > max) {
                max = nums[i];
            }
            post[i] = max;
        }
        for (int i = 1; i < n - 1; i++) {
            if (pre[i - 1] < nums[i] && post[i + 1] > nums[i]) {
                return true;
            }
        }
        return false;
    }

    static public boolean increasingTriplet(int[] nums) {
        if (nums == null || nums.length < 3) {
            return false;
        }
        //if this looks too fragile you could iterate over nums to find its maximum. Wanted to keep this as a one-time read solution
        int n = nums.length;
        int min1 = Integer.MAX_VALUE;
        int min2 = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            if (nums[i] <= min1) {
                min1 = nums[i];
            } else if (nums[i] <= min2) {
                min2 = nums[i];
            } else {
                return true;
            }

        }
        return false;
    }

    static public void main(String args[]) {
        int x[] = {0, 4, 2, 1, 0, -1, -3};
        System.out.print(increasingTriplet(x));
    }
}
