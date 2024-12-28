
public class J172 {
        // public double factorial(double n) {
        //     if(n == 0) {return 1;}
        //     n = n * factorial(n-1);
        //     return n;
        // }
        public int trailingZeroes(int n) {
            if(n == 0) {return 0;}
            double extras = Math.floor(Math.log(n)/Math.log(5));
            int total = 0;
            while(extras > 0) {
                double num = Math.pow(5,extras);
                total += n/num;
                extras--;
            }
            

            return total;
        }
        
    public static void main(String args[]) {
        J172 hire = new J172();
        System.out.print(hire.trailingZeroes(50));
    }
}
