import java.util.*;
public class J1004 {
  
    public int longestOnes(int[] nums, int k) {
        int max = 0;
       //expand around center sliding window
       //use a set
       int[] temp = new int[nums.length];
       int count = 0;
        for(int i = 0; i < nums.length;i++) {
            if(nums[i] == 0) {temp[count] = i;count++;}
        }

        Set<List<Integer>> nodups = new HashSet<List<Integer>>();

        for(int i = 0; i  < count; i++) {
            for(int j = 0; j < count; j++) {
                List<Integer> s = new ArrayList<Integer>(); 
                s.add(temp[j]);
                
                nodups.add(s);
            }
           
        }
       
        for(List<Integer> i : nodups) {
            for(int j : i) {
                System.out.print(j + " ");
            }
            System.out.println();
        }
        return max;

    }
    public static void main(String args[]) {
        J1004 h = new J1004();
        int[] t = {1,1,1,0,0,0,1,1,1,1,0};
        System.out.println(h.longestOnes(t, 2));
    }
}


/*
 * 
 * if(nums.length <= 3) {
            for(int i : nums) {
                if(i == 1 && k > 0) {
                    max++;
                }
                else {k--;}
            }
            return max;
        }

       for(int i = 1; i < nums.length; i++) {
        int counter = k;
        if(nums[i] != 1) {counter--;}
        int left = i, right = i;
        boolean hasLeft = left > 0;
        boolean hasRight = right < nums.length-1;
        while(counter > 0) {
            if(hasLeft) {
                left--;
                if(nums[left] != 1) {
                    counter--;
                    left--;
                }
                while(left > 0 && nums[left] == 1) {
                if(nums[left] != 1) {break;}
                left--;
                    }
                }
            if(counter <= 0) {break;}
            if(hasRight) {
                right++;
                if(nums[right] != 1) {
                    counter--;
                    right++;
                }
                    while(right < nums.length && nums[right] == 1) {
                            if(nums[right] != 1) {break;}
                            right++;
        }
    }

        else break;

        hasRight = right < nums.length-1;
        hasLeft = left > 0;
    }
            
            
          
            int subMax = right - left - 1;
            if(max < subMax) {max = subMax;}
        

       }
       return max;
 */