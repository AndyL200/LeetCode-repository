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
            for(int i : x) {
                Node newNode = new Node(i,x[i]);
                current.link = newNode;
                current = newNode;
                 
            }
        }
        public void remove(int toRemv) {
            Node current = this.head;
            while(current != null) {
                if(current.link != null && current.link.item == toRemv ) {
                    current.link = current.link.link;
                }
                current = current.link;
            }
            
        }
    }
    public int maxArea(int[] height) {
        int largestArea = 0, avg = findAvg(height);
        Node heightList = new Node();
        heightList.arrayToList(height);
        Node outerCurrent = heightList.head;
        while(outerCurrent != null) {
            Node innerCurrent = heightList.head;
            while(innerCurrent != null) {
                if(outerCurrent.item < avg) {heightList.remove(outerCurrent.item); break;}
                int area = Math.abs(outerCurrent.index - innerCurrent.index)*Math.min(innerCurrent.item, outerCurrent.item);
                if(largestArea < area) {
                largestArea = area;
                }
                innerCurrent = innerCurrent.link;
            }
            outerCurrent = outerCurrent.link;
        }
        return largestArea;
    }

    public int findAvg(int[] x) {
        int sum = 0;
        int count = 0;
        for(int i = 0; i < x.length;i++) {
            sum = sum + x[i];
            count++;
        }
        return sum/count;
    }


    public static void main(String args[]) {
        J11 hire = new J11();
        int[] bogg = {1,8,6,2,5,4,8,3,7};
        System.out.println(hire.maxArea(bogg));
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