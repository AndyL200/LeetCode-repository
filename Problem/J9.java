
class J9 {

    public static boolean isPalindrome(int x) {
        int mutable = x;
        int num = 0;
        if (x < 0) {
            return false;
        }
        while (mutable > 0) {
            int digit = mutable % 10;
            num = num * 10 + digit;
            mutable = mutable / 10;
        }
        return (x == num);
    }

    public static void main(String args[]) {

    }
}
