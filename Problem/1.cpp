#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

class Solution
{
public:
    vector<int> twoSum(vector<int> &nums, int target)
    {
        vector<int> res;
        unordered_map<int, int> hash;
        for (int i = 0; i < nums.size(); i++)
        {
            if (hash.find(nums[i]) != hash.end())
            {
                res.push_back(i);
                res.push_back(hash.at(nums[i]));
                return res;
            }
            else
            {
                int numToFind = target - nums[i];
                hash.insert({numToFind, i});
            }
        }
        return res;
    }
};