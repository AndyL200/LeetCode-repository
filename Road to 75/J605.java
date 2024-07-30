
class J605 {
        public int[] arraySizeMaxing(int[] x, int s) {
            int[] b = new int[x.length+s];
            return b;
        }   
    
        public boolean canPlaceFlowers(int[] flowerbed, int n) {
    
            
            for (int i = 0; i < flowerbed.length; i++) {
                    if(flowerbed[i] == 0 && (i == 0 || flowerbed[i-1] == 0) && (i == flowerbed.length-1 || flowerbed[i+1] == 0)) {
                    flowerbed[i] = 1;
                    n--;
                    }
            }
    
    
            if (n <= 0) {
                return true;
            } else {
                return false;
            }
    
        }
        
    public static void main(String args[]) {
        int[] j = { 1, 0, 0, 0, 1 };
        J605 hire = new J605();
        System.out.println(hire.canPlaceFlowers(j, 2));
    }
}