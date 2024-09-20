public class J645 {
//Sliding window
public double findMaxAverage(int[] nums, int k) {
    double maxAvg = 0;
     double sum = 0;
     for(int j = 0; j < k;j++) {
            sum = sum +  nums[j];
        }

        double avg = sum/k;
        if(maxAvg < avg) {maxAvg = avg;}
    int i = 1;
    while(i + k <= nums.length) {
       sum = sum - nums[i-1];
       sum = sum + nums[k+i-1];
        avg = sum/k;
        if(maxAvg < avg) {maxAvg = avg;}
        i++;
    }
    return maxAvg;
}
public static void main(String args[]) {
    int[] x = {1,12,-5,-6,50,3};
    J645 hire = new J645();
    System.out.println(hire.findMaxAverage(x, 4));
}
}
