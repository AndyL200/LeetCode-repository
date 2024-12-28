import java.util.*;
public class J282 {
        public int mapping(char c) {
            switch(c){
                case '0': return 0;
                case '1': return 1;
                case '2': return 2;
                case '3': return 3;
                case '4': return 4;
                case '5': return 5;
                case '6': return 6;
                case '7': return 7;
                case '8': return 8;
                case '9': return 9;
                default: return 0;
            }
    }
        public void nesting(String num, int target, int end, List<String> x) {
            int sub = target;
            int div = target;
    
            if(end >= 0) {
            
            sub -= mapping(num.charAt(end));
            try{
            div /= mapping(num.charAt(end));
            }
            catch(Exception DivideByZeroException) {
                return;
            }
            char[] str = num.toCharArray();
            char c = str[end];
            str[end] = '+';
            for(int i = end+1; i < num.length();i++) {
                char temp = str[i];
                str[i] = c;
                c = temp;
            }
            String res1 = new String(str);
            nesting(res1, sub, end-2, x);
    
            str = num.toCharArray();
            c = str[end];
            str[end] = '*';
            for(int i = end+1; i < num.length();i++) {
                char temp = str[i];
                str[i] = c;
                c = temp;
            }
            String res2 = new String(str);
            nesting(res2, div, end-2, x);




            }
            if(sub == 0  && end < 0) {x.add(num);}

        }
        public List<String> addOperators(String num, int target) {
            List<String> x = new ArrayList<String>();
            nesting(num, target, num.length()-1, x);
            return x;
        }
        public static void main(String args[]) {
            List<String> res = new ArrayList<String>();
            J282 hire = new J282();
            res = hire.addOperators("18732947238", 1782);
            for(String s : res) {
                System.out.println(s);
            }
        }

    }

