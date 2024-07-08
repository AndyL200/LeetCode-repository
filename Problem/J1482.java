
class J1482 {







    public int minDays(int[] bloomDay, int m, int k) {
        int bouquetrunning = 0;
        int bouquets = -1;
        int runningIndex[] = new int[bloomDay.length];
        int count;
        int days;
        for(days = 0; days < findMaxIndex(bloomDay); days++) {
            count = 0;
            bouquetrunning = 0;
            if(bouquets >= m) {
                break;
            }
        for(int x = 0; x < bloomDay.length; x++ ) {
            if(bloomDay[x] <= days && bloomDay[x] > 0) {
                bouquetrunning++;
                runningIndex[count] = x;
                count++;
            }
            if(bouquetrunning == m) {
                bouquets++;
                for(int i = 0; i < runningIndex.length; i++) {
                    bloomDay[runningIndex[i]] = 0;
                }
            }
        }
        
    }

            return days;


    }
    public int findMaxIndex(int[] c) {
        int i = 1;
        int max = 0;
        while(i < c.length) {
            if(c[i] > max) {
                max = c[i];
            }
            i++;
        }
        return max;
    }
    public static void main(String args[]) {
        J1482 hire = new J1482();
        int[] bloomDay = {1,10,3,10,2};
        System.out.println(hire.minDays(bloomDay, 3, 1));
    }
}