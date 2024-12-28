
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;

public class J2215 {

    public static List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        List<List<Integer>> list = new ArrayList<>();

        HashSet<Integer> distinct1 = new HashSet<>();
        HashSet<Integer> distinct2 = new HashSet<>();

        for (int i : nums1) {
            distinct1.add(i);
        }
        for (int i : nums2) {
            distinct2.add(i);
        }

        for (int i : nums2) {
            if (distinct1.contains(i)) {
                distinct1.remove(i);
                distinct2.remove(i);
            }
        }

        list.add(new ArrayList<>(distinct1));
        list.add(new ArrayList<>(distinct2));
        return list;

    }

    public static void main(String args[]) {
        int[] num1 = {1, 2, 3}, num2 = {2, 4, 6};
        System.out.print(findDifference(num1, num2));
    }
}
