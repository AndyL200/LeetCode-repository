#include <iostream>
#include <vector>

using namespace std;

// literally just a quicksort?

int partition(vector<int> &nums, int low, int high)
{

    int i = low - 1;
    for (int j = low; j < high; j++)
    {
        if (nums[j] < nums[high])
        {
            i++;
            swap(nums[i], nums[j]);
        }
    }
    swap(nums[i + 1], nums[high]);
    return (i + 1);
}
void quicksort(vector<int> &nums, int low, int high)
{

    if (low < high)
    {

        int p = partition(nums, low, high);
        quicksort(nums, p + 1, high);
        quicksort(nums, low, p - 1);
    }
}
void quicksort(vector<int> &nums)
{
    quicksort(nums, 0, nums.size() - 1);
}

void sortColors(vector<int> &nums)
{
    quicksort(nums);
}

int main()
{
    vector<int> n = {2, 0, 2, 1, 1, 0};
    sortColors(n);
}