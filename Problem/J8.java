public class J8 {

    boolean isInteger(char c) {
        boolean truthy;
        if((int)c >= 48 && (int)c < 58) {
            truthy = true;
        }
        else {
            truthy = false;
        }
        return truthy;
    }
    boolean cleanStringandFindSign(String s) {
        String clean = "";
        for(char c : s.toCharArray()) {
            if(c != ' ') {clean += c;}
        }
        s = clean;
        if(s.charAt(0) == '-') {
            return false;
        }
        else {return true;}
    }
    public int myAtoi(String s) {
        int result = 0, placeholder = 1;
        int max = s.length();
        boolean stop = true;
        boolean sign = cleanStringandFindSign(s);
        for(int i = 0; i < max; i++) {
            
            if(stop && isInteger(s.charAt(i)) && true) {
                result += ((int)s.charAt(i) - 48) * Math.pow(10,max - placeholder);
                
            }
            else {
                result = result/10;
            }
            placeholder++;

            if(result != 0 && isInteger(s.charAt(i)) == false) {
                stop = false;
            }
            
        }
        if(sign) {
        return result;
        }
        else {
            return result/-1;
        }
    }

    public static void main(String args[]) {
        J8 item = new J8();
        System.out.println(item.myAtoi("     1234cgft"));
    }
}
