public class J88<T> {

 
    
    public int partition(int []x, int low, int high) {
         int pivot = x[high];
         int i = low - 1;

         for(int j = low; j < high; j++) {
            if(x[j] >= pivot) {
                i += 1;
                int temp = x[i];
                x[i] = x[j];
                x[j] = temp;
            }
         }
         i++;
         int temp = x[i];
         x[i] = x[high];
         x[high] = temp;
         return i+1;

    }
    public void Qsort(int[] x, int low, int high) {
        if(high == -1) {
           high = x.length -1;
        }


        if(low < high) {
            int pivIndex = partition(x, low, high);
            Qsort(x, low, pivIndex-1);
            Qsort(x, pivIndex+1, high);
        }
    }
    
        public void merge(int[] nums1, int m, int[] nums2, int n) {
            for(int i = 0, j = m;  i < n;  i++, j++) {
                nums1[j] = nums2[i];
    
            }
            Qsort(nums1, 0, -1);
        }

        public static void main(String args[]) {
            J88<Integer> hire = new J88<Integer>();
            int[] nums1 = {2,4,6,0,0,0};
            int[] nums2 = {1,9,8};
            hire.merge(nums1, nums1.length-nums2.length, nums2, nums2.length);
            for (int x : nums1) {
                System.out.println(x);
            }
            
        }
    
}
