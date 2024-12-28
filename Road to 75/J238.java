import java.util.Arrays;

public class J238 {
    //naive
    static public int[] product(int[] s) {
        int n = s.length;
        int[] postfix = new int[n + 1];
        postfix[n] = 1;
        int[] prefix = new int[n+1];
        prefix[0] = 1;
        for(int i = 1; i < n + 1; i++) {
            prefix[i] = prefix[i-1] * s[i-1];
        }
        for(int i = n; i > 0; i--) {
            postfix[i-1] = s[i-1]*postfix[i];
        }
        int[] answer = new int[n];
        for(int i = 0; i < n; i++) {
            answer[i] = prefix[i] * postfix[i+1];
        }        
        return answer;
    }
    static public int[] productExceptSelf(int[] s) {
        int n = s.length;
        int[] output = new int[n];
        int total = 1;

        for(int i = 0; i < n; i++) {
            output[i] = total;
            total = total * s[i];
        }
        total = 1;
        for(int i = n-1; i >= 0; i--) {
            output[i] = output[i] * total;
            total = total*s[i];
        }
        return output;
    }

    static public void main(String args[]) {
        int[] p = {1,2,3,4};
        System.out.println( Arrays.toString(productExceptSelf(p)) );
    }
}
