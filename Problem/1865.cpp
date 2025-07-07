#include <vector>
#include <unordered_map>
using std::unordered_map;
using std::vector;
class FindSumPairs
{
public:
    vector<int> nums1;
    vector<int> nums2;
    unordered_map<int, int> um1;
    unordered_map<int, int> um2;
    FindSumPairs(vector<int> &nums1, vector<int> &nums2)
    {
        this->nums1 = nums1;
        this->nums2 = nums2;

        unordered_map<int, int> u1;
        for (int i : nums1)
        {
            if (u1.find(i) == u1.end())
                u1[i] = 1;
            else
                u1[i] += 1;
        }
        this->um1 = u1;
        unordered_map<int, int> u2;
        for (int i : nums2)
        {
            if (u2.find(i) == u2.end())
                u2[i] = 1;
            else
                u2[i] += 1;
        }
        this->um2 = u2;
    }

    void add(int index, int val)
    {
        if (um2[nums2[index]] > 1)
            um2[nums2[index]] -= 1;
        else
            um2.erase(nums2[index]);

        nums2[index] += val;
        if (um2.find(nums2[index]) != um2.end())
            um2[nums2[index]] += 1;
        else
            um2[nums2[index]] = 1;
    }

    int count(int tot)
    {

        int count = 0;

        for (auto it : um1)
        {
            if (um2.find(tot - it.first) != um2.end())
                count += um2[tot - it.first] * it.second;
        }
        return count;
    }
};

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * FindSumPairs* obj = new FindSumPairs(nums1, nums2);
 * obj->add(index,val);
 * int param_2 = obj->count(tot);
 */