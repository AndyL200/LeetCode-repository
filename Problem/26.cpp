#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;


    int removeDuplicates(vector<int>& nums) {
        int curr = 0;
        for(int i = 1; i < nums.size(); ++i)
        {
            if(nums[i-1] == nums[i])
            continue;
            else {
                ++curr;
                nums[curr] = nums[i];
            }
        }
        return curr+1;
    }