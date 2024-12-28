
class J374 {

    public int guessNumber(int n) {
        int high = n, low = 1;
        int mid = (high + low) / 2;

        while (low <= high) {
            mid = low + (high - low) / 2;
            int i = guess(mid);
            if (i == -1) {
                high = mid + 1;
            } else if (i == 1) {
                low = mid - 1;
            } else {
                return mid;
            }
            mid = (high + low + 1) / 2;
            i = guess(mid);
        }
        return -1;
    }

}
