public class J11On {
    public static int containerMax(int[] n) {
        int max = 0;
        int a = 0;
        int b = n.length-1;
        int height = 0, width = 0;
        while(a < b) {
             height = Math.min(n[a],n[b]); 
             width = b-a;
            max = Math.max(max,height*width);
            if(height == n[a]) {a++;}
            else {b--;}
            }

        return max;
    }

    public static void main(String args[]) {
        int[] b = {6,9,3,4,5,8};
        System.out.print(containerMax(b));
    }
}
