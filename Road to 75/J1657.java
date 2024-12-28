
import java.util.Arrays;
import java.util.HashMap;

public class J1657 {

    //naive
    public static boolean close(String word1, String word2) {
        int w1 = word1.length(), w2 = word2.length();
        if (w1 != w2) {
            return false;
        }
        char[] c1 = word1.toCharArray();
        char[] c2 = word2.toCharArray();

        HashMap<Character, Integer> m1 = new HashMap<>();
        HashMap<Character, Integer> m2 = new HashMap<>();

        for (char c : c1) {
            if (m1.containsKey(c)) {
                m1.put(c, m1.get(c) + 1);
            } else {
                m1.put(c, 1);
            }
        }
        for (char c : c2) {
            if (m2.containsKey(c)) {
                m2.put(c, m2.get(c) + 1);
            } else {
                m2.put(c, 1);
            }
        }

        if (!m1.keySet().equals(m2.keySet())) {
            return false;
        }
        HashMap<Integer, Integer> f1 = new HashMap<>();
        HashMap<Integer, Integer> f2 = new HashMap<>();

        for (int i : m1.values()) {
            f1.put(i, f1.getOrDefault(i, 0) + 1);
        }
        for (int i : m2.values()) {
            f2.put(i, f2.getOrDefault(i, 0) + 1);
        }
        return f1.equals(f2);

    }

    public static boolean closeStrings(String word1, String word2) {
        int[] freq1 = new int[26];
        int[] freq2 = new int[26];

        for (char c : word1.toCharArray()) {
            freq1[c - 'a']++;
        }
        for (char c : word2.toCharArray()) {
            freq2[c - 'a']++;
        }

        for (int i = 0; i < 26; i++) {
            if ((freq1[i] == 0 && freq2[i] != 0) || (freq1[i] != 0 && freq2[i] == 0)) {
                return false;
            }
        }

        //only the frequencies matter, let's us iterate over different character contexts at once
        Arrays.sort(freq1);
        Arrays.sort(freq2);

        for (int i = 0; i < 26; i++) {
            if (freq1[i] != freq2[i]) {
                return false;
            }
        }
        return true;
    }

    public static void main(String args[]) {
        String word1 = "abbzzca", word2 = "babzzcz";
        System.out.print(closeStrings(word1, word2));
    }
}
