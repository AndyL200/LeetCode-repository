
//this is my code along for neetcode's mock interview from this video : https://youtu.be/46dZH7LDbf8


public class neetcodeIntQuestion {
    int[] x = {};
    
    public int[] enlarge(int[] x, int s) {
        int b[] = new int[s + x.length];
        for(int i = 0; i < x.length; i++ ) {
            b[i] = x[i];
        }
        return b;
    }
    public int[] delarge(int[] x, int s) { //these functions make the code more scalable if I wanted to overload my insert method to handle more than one value
        int b[] = new int[x.length - s];
        for(int i = 0; i < x.length - s; i++) {
            b[i] = x[i];
        }
        return b;
    }

    public void insert(int k) {
        boolean duplicate = false;
        for(int i = 0; i < x.length; i++) {
            if(x[i] == k) {
                duplicate = true;
                break;
            }
        }
        if(duplicate == false) {
        x  = enlarge(x, 1);
        x[x.length-1] = k;
        } 
    }
    public void remove(int k) {
        for(int i = 0; i < x.length; i++){
            if(x[i] == k) {
                for(int j = i; j < x.length-1; j++) {
                    int temp = x[j];
                    x[j] = x[j+1];
                    x[j+1] = temp;
                }
                break;
            }
        }
        x = delarge(x, 1); //One for the non overloaded method
    }

    //Sample overloaded method
    public void insertblah(int[] c) {
        //pass c.length to enlarge
    }

    public int getRandom() {
        double random = (x.length-1)*Math.random();
        return x[(int)Math.round(random)];
    }
    public void print() {
        for(int i : this.x) {
        System.out.println(i + " ");
        }
    }

    public static void main(String args[]) {
        long start = System.nanoTime();
        neetcodeIntQuestion hire = new neetcodeIntQuestion();
        hire.insert(1);
        hire.insert(2);
        hire.insert(5);
        hire.insert(6);
        hire.insert(5);
        hire.insert(8);
        hire.remove(1);
        System.out.println(hire.getRandom() + " (This is a random number)");
        hire.print();
        long end = System.nanoTime();
        System.out.print((end - start)/1000000 + "ms (This checks the runtime for my code)");

    }
}
