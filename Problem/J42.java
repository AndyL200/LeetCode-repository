public class J42 {
    // public static int expand(int[] h, int center) {
    //     int l = 0, r = 0;
    //     for(int i = center; i < h.length;i++) {
    //         if(h[i] > r) {r = h[i];}
    //     }
    //     for(int i = 0; i < center; i++) {
    //         if(h[i] > l) {l = h[i];}
    //     }
    //     int res = Math.min(l,r) - h[center];
    //     return (res > 0)? res : 0;




    // for(int i = 0;i < height.length; i++) {

            
    //     int maxRight = height[i], maxLeft = height[i], l = i, r = i;
    //   while(l >= 0){maxLeft = Math.max(maxLeft, height[l]); l--;}
    //   while(r < height.length){maxRight = Math.max(maxRight, height[r]); r++;}
    //   int current = Math.min(maxLeft,maxRight) - height[i];
    //   total += (current > 0)? current : 0;
    // }
    // }
    public static int trap(int[] height) {
        
        int total = 0;
        int maxRight = 0, maxLeft = 0, a = 0, b = height.length-1;
        while(a < b) {
            if(height[a] <= height[b]) { 
                if(maxLeft > height[a]) {
                    total += maxLeft - height[a]; 
                }
                //do we have a wall on the right?
                maxLeft = Math.max(maxLeft, height[a]);
                a++; //do we calculate?
            }
            else {
                if(maxRight > height[b]) {
                    total += maxRight - height[b];
                }
                maxRight = Math.max(maxRight, height[b]);
                b--;
            }
            
        }
       

        return total;

    }
    public static void main(String args[]) {
        int n[] = {0,1,0,2,1,0,1,3,2,1,2,1};
        System.out.print(trap(n));
    }
}
/*
 * int l,r;
        int runningArea = 0;
        for(int i = 1; i < height.length-1; i++) {
            l = i-1;
            r = i;
            if(height[l] > height[i]) {
                while(r < height.length-1 && height[r] <= height[i]) {
                    r++;
                }
                if(r == height.length-1 && height[r] <= height[i]) {r=i;}
                runningArea += (r-i) * Math.min(height[l]-height[i],height[r]-height[i]);
            }
        }
        return runningArea;




        int maxArea = 0;
        int a = 0, b = height.length-1;
        int i1 = 0,i2 = 0;
        int l = 0,w = 0;
        while(a < b) {
            l = Math.min(height[a],height[b]);
            w = b-a-1;
            if(l*w > maxArea) {maxArea = l*w; i1 = a; i2 = b;}
            if(l == height[a]) {
                a++;
            }
            else {
                b--;
            }
        }
        for(int i = i1+1; i < i2-1; i++) {
            if(height[i] > l) {height[i] = l;}
            maxArea -= height[i];
        }
        return maxArea;



         for(int i = 0;i < height.length; i++) {
            r = i;  
          maxRight = height[i];
          maxLeft = Math.max(maxLeft, height[i]);
          while(r < height.length){maxRight = Math.max(maxRight, height[r]); r++;}
          int current = Math.min(maxLeft,maxRight) - height[i];
          total += (current > 0)? current : 0;
        }
 */