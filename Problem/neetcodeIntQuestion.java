
//this is my code along for neetcode's mock interview from this video : https://youtu.be/46dZH7LDbf8


public class neetcodeIntQuestion {
    int[] x = {};
    
    public int[] enlarge(int[] x, int s) {
        int b[] = new int[s + x.length];
        for(int i = 0; i < x.length; i++ ) {
            b[i] = x[i];
        }
        return b; //could theorectically make this faster using a dynamic cache system that changes allocation based on how much you are inserting
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


    public void foreignRemoveShift(int[] c, int val) {
        for(int i = 0; i < x.length; i++){
            if(x[i] == val) {
                for(int j = i; j < x.length-1; j++) {
                    int temp = x[j];
                    x[j] = x[j+1];
                    x[j+1] = temp;
                }
                break;
            }
        }
    }

    //Sample overloaded method
    public void insert(int[] c) {
        int matchmaker;
        int outOfScope = 0;
        for(int i = 0; i < c.length; i++) {
            matchmaker = 0;
            for(int k = 0; k < c.length; k++) {
                if(c[i] == c[k]) {
                    matchmaker++;
                }
                if(matchmaker > 2) {
                    foreignRemoveShift(c, c[i]);
                    outOfScope++;
                }
            }
            }
        c = delarge(c, outOfScope);

            outOfScope = 0;
        for(int i = 0; i < x.length; i++) {
            for(int j = 0; j < c.length-outOfScope;j++) {
                if(j == i) {
                    foreignRemoveShift(c, j);
                    outOfScope++;
                }
            }
        }
        c = delarge(c, outOfScope);
        //pass c.length to enlarge
        int endofX = x.length;
        x = enlarge(x, c.length);
        for(int i = endofX, j = 0; i < x.length && j < c.length;i++, j++) {
            x[i] = c[j];
        }
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
        hire.insert(1);
        hire.insert(2);
        hire.insert(1);
        hire.insert(2);
        hire.remove(1);
        System.out.println(hire.getRandom() + " (This is a random number)");
        // int[] pls = {1,2,3,4,5,6,7,8,9,12,15,16,27,24,32,68,97};
        // hire.insert(pls);
        hire.print();
        
        long end = System.nanoTime();
        System.out.print((end - start)/1000000 + "ms (This checks the runtime for my code)");

    }
}
