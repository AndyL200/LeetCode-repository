public class J11 {

    class Node {
        int index;
        int item;
        Node link;
        Node head;
        Node(int index, int item) {
            this.index = index;
            this.item = item;
            this.link = null;
        }
        Node() {

        }
        public void Append() {}
        public void arrayToList(int[] x) {
            Node current = new Node(0,x[0]);
            this.head = current;
            for(int i = 0; i < x.length; i++) {
                Node newNode = new Node(i,x[i]);
                current.link = newNode;
                current = newNode;
                 
            }
        }
        public void removeLessThanAvg(int avg) {
            Node current = this.head;
            while(current != null) {
                if(current.link != null && current.link.item < avg) {
                    current.link = current.link.link;
                }
                current = current.link;
            }
        }
        public void remove(Node toRemv) {
            Node current = this.head;
            while(current.link != null && current.link != toRemv) {
                current = current.link;
            }
            if(current.link == toRemv) {
                current.link = current.link.link;
                current = current.link;
            }
        }
    }

    

    public int maxArea(int[] height) {
        int largestArea = 0;
        Node heightList = new Node();
        heightList.arrayToList(height);
        heightList.removeLessThanAvg(findAvg(heightList));
        Node outerCurrent = heightList.head;
        while(outerCurrent != null) {
            Node innerCurrent = heightList.head;
            while(innerCurrent != null) {
                int area = Math.abs(outerCurrent.index - innerCurrent.index)*Math.min(outerCurrent.item,innerCurrent.item);
                if(largestArea < area) {
                largestArea = area;
                }
                innerCurrent = innerCurrent.link;
            }
            heightList.removeLessThanAvg(findAvg(heightList));
            outerCurrent = outerCurrent.link;
            
        }
        return largestArea;
    }

    public int findAvg(Node node) {
        int sum = 0;
        int count = 0;
        Node current = node.head;
        while(current != null) {
            sum = sum + current.item;
            count++;
            current = current.link;
        }
        return sum/count;
    }


    public static void main(String args[]) {
        long startTime = System.nanoTime();
        J11 hire = new J11();
        int[] bogg = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,185,186,187,188,189,190,191,192,193,194,195,196,197,198,199,200,201,202,203,204,205,206,207,208,209,210,211,212,213,214,215,216,217,218,219,220,221,222,223,224,225,226,227,228,229,230,231,232,233,234,235,236,237,238,239,240,241,242,243,244,245,246,247,248,249,250,251,252,253,254,255,256,257,258,259,260,261,262,263,264,265,266,267,268,269,270,271,272,273,274,275,276,2};
        System.out.println(hire.maxArea(bogg));
        long endTime = System.nanoTime();
        long duration =  endTime - startTime;
        System.out.println(duration/1000000);
    }

}

/*
 * int max = 0, secondhighest = 0, range = 999999999, index = 0;
        for(int i = 0; i < height.length; i++) {
            int temp = range;
            if(height[i] > max) {
            max = height[i];
            index = i;
            }
            else {
                range = max - height[i];
            }
            if(range < temp) {
            secondhighest = max - range;
            }
        }
        int secondHighIdx = findIndex(height, secondhighest);

        if(secondhighest == 0) {return max*Math.abs(index-secondHighIdx);}
        else {return secondhighest*Math.abs(index-secondHighIdx);}
    }
    public int findIndex(int[] x, int item) {
        for(int i : x) {
            if(item == x[i]) {
                return i;
            }
        }
        return -1;
    }

 */