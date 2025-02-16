#include <iostream>
#include <vector>
using namespace std;
vector<int> twoSum(vector<int> &numbers, int target)
{
    int l = 0;
    int h = numbers.size() - 1;
    int s = numbers[l] + numbers[h];
    while (s != target)
    {
        if (s < target)
        {
            l++;
        }
        else if (s > target)
        {
            h--;
        }
        s = numbers[l] + numbers[h];
    }
    return {l + 1, h + 1};
}