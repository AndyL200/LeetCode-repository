import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.atomic.AtomicInteger;

public class J70Better {
        public boolean isTwo(List<Integer> F) {
            int howManyOnes = 0;
            for(int i : F) {
                    if(i == 1) {
                        howManyOnes++;
                    }
            }
            if(howManyOnes > 1) {
                return true;
            } 
            else {
                return false;
            }
        
        }

        public double factorial(double n) {
            if(n <= 1) { return 1;}
            if(n > 1 ) {
                n = n * factorial(n-1);
            }
            return n;
        }

        public int climbStairs(int n) {
            List<Integer> F = new ArrayList<Integer>();
            while(n > 0) {
                F.add(1);
                n--;
            }

            double ist = 1;
            int end = F.size();
            int i = 0;
            while(isTwo(F)) {
                F.set(i,2);
                i++;
                end--;
                ist = ist + factorial(end)/(factorial(i) * factorial(end-i));
                F = F.subList(0,end);
            }
            return (int)ist;

            }
            
            public static boolean isValid(String str) {
                int i = 0;
            while(i < str.length()) {
                int j = i;
                while(str.charAt(i) != '.') {i++;}
                if(Integer.valueOf(str.substring(j,i)) < 0 || Integer.valueOf(str.substring(j,i)) > 255) {return false;}
                i++;
            }        
            return true;
            }

            public static void main(String args[]) {
                J70Better hire = new J70Better();
                System.out.println(hire.factorial(30)/hire.factorial(27));
                // System.out.println(hire.climbStairs(33));

            }
}
