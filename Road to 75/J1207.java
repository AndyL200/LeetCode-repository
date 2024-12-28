
import java.util.HashMap;
import java.util.HashSet;

public class J1207 {

    public static boolean uniqueOccurrences(int[] arr) {

        HashMap<Integer, Integer> h1 = new HashMap<>();
        for (int i : arr) {
            if (h1.containsKey(i)) {
                h1.put(i, h1.get(i) + 1);
            } else {
                h1.put(i, 0);
            }
        }
        HashSet<Integer> distinct = new HashSet<>();
        for (int i : h1.values()) {
            if (distinct.contains(i)) {
                return false;
            }
            distinct.add(i);
        }

        return true;

    }

    public static void main(String args[]) {
        int[] h = {1, 2};
        System.out.print(uniqueOccurrences(h));
    }
}
