import java.util.HashMap;
import java.util.Map;

public class J273 {
    
    Map<Integer, String> integers = new HashMap<Integer, String>();
    Map<Integer, String> decimalPlaces = new HashMap<Integer, String>();
    Map<Integer, String> shortHands = new HashMap<Integer, String>();

    J273() {
    integers.put(1, "One");
    integers.put(2, "Two");
    integers.put(3, "Three");
    integers.put(4, "Four");
    integers.put(5, "Five");
    integers.put(6, "Six");
    integers.put(7, "Seven");
    integers.put(8, "Eight");
    integers.put(9, "Nine");
    integers.put(0, "Zero");

    decimalPlaces.put(2, "Hundred");
    decimalPlaces.put(3, "Thousand");
    decimalPlaces.put(6, "Million");

    shortHands.put(10, "Ten");
    shortHands.put(20, "Twenty");
    shortHands.put(30, "Thirty");
    shortHands.put(40, "Fourty");
    shortHands.put(50, "Fifty");
    shortHands.put(60, "Sixty");
    shortHands.put(70, "Seventy");
    shortHands.put(80, "Eighty");
    shortHands.put(90, "Ninety");
}

        public String numberToWords(int num) {
            int x = 10, placement = 0;
            String result = "";
                while(num / x > 1) { 
                    x *= 10;
                    if(decimalPlaces.containsKey(placement)) {
                        result += decimalPlaces.get(placement);
                    }
                    else if(decimalPlaces.keySet())
                    placement++;
                   
                }

        }
    
}