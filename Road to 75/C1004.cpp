#include <iostream>
#include <vector>

using namespace std;

int longestOnes(vector<int> &nums, int k)
{
    int max = 0;
    int l = 0, r = 0;
    // find subset with most ones

    while(r < nums.size()) { 
        k -= 1 - nums[r]; 
        if(k < 0) {k += 1 - nums[l]; l++; }
        else {max = (max < r-l+1)? r-l+1 : max;}
        r++;
    }
    return max;
}

int main()
{
    vector<int> n = {0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1};
    cout << longestOnes(n, 3);
    return 1;
}