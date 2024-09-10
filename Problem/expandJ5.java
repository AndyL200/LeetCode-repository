

public class expandJ5 {

  
    public static String longestPalindrome(String x) {
        String longest = "";
        for(int i = 0; i < x.length(); i++) {



            int l = i,r = i;
            while(l >= 0 && r < x.length() && x.charAt(l) == x.charAt(r)) {
                String palindrome1 = x.substring(l, r+1);
                if(palindrome1 == "nyn") {
                    System.out.println("here");
                }

                if(palindrome1.length() > longest.length()) {
                    longest = palindrome1;
                }
                l--;
                r++;
            }

            l = i; r = i+1;
            while(l >= 0 && r < x.length() && x.charAt(l) == x.charAt(r)) {
                String palindrome2 = x.substring(l, r+1);
                if(palindrome2.length() > longest.length()) {
                    longest = palindrome2;
                }
                l--;
                r++;
            }
            
            
        }
        return longest;
    }

    public static void main(String args[]) {
        System.out.print(longestPalindrome("civilwartestingwhetherthatnaptionoranynartionsoconceivedandsodedicatedcanlongendureWeareqmetonagreatbattlefiemldoftzhatwarWehavecometodedicpateaportionofthatfieldasafinalrestingplaceforthosewhoheregavetheirlivesthatthatnationmightliveItisaltogetherfangandproperthatweshoulddothisButinalargersensewecannotdedicatewecannotconsecratewecannothallowthisgroundThebravelmenlivinganddeadwhostruggledherehaveconsecrateditfaraboveourpoorponwertoaddordetractTgheworldadswfilllittlenotlenorlongrememberwhatwesayherebutitcanneverforgetwhattheydidhereItisforusthelivingrathertobededicatedheretotheulnfinishedworkwhichtheywhofoughtherehavethusfarsonoblyadvancedItisratherforustobeherededicatedtothegreattdafskremainingbeforeusthatfromthesehonoreddeadwetakeincreaseddevotiontothatcauseforwhichtheygavethelastpfullmeasureofdevotionthatweherehighlyresolvethatthesedeadshallnothavediedinvainthatthisnationunsderGodshallhaveanewbirthoffreedomandthatgovernmentofthepeoplebythepeopleforthepeopleshallnotperishfromtheearth"));
    }
}
