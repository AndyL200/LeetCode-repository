#include <iostream>
#include <vector>

using namespace std;

int partition(vector<int> &nums, int low, int high)
{
    int pivot = nums[high];

    int i = low - 1;
    int j = low;
    while (j < high)
    {
        if (nums[j] < pivot)
        {
            ++i;
            swap(nums[i], nums[j]);
        }
        j++;
    }
    swap(nums[i + 1], nums[high]);
    return i + 1;
}
void quickSort(vector<int> &nums, int low, int high)
{

    if (low < high)
    {

        int p = partition(nums, low, high);
        quickSort(nums, low, p - 1);
        quickSort(nums, p + 1, high);
    }
}
void permSort(vector<int> &nums, int p)
{
    quickSort(nums, p, nums.size() - 1);
}
void nextPermutation(vector<int> &nums)
{
    int a = -1;
    for (int i = 0; i < nums.size() - 1; i++)
    {
        if (nums[i] < nums[i + 1])
        {
            a = i;
        }
    }
    if (a == -1)
    {
        permSort(nums, 0);
        return;
    }
    int m = 101;
    int b = -1;
    for (int i = a + 1; i < nums.size(); i++)
    {
        if (nums[i] > nums[a] && nums[i] < m)
        {
            m = nums[i];
            b = i;
        }
    }
    swap(nums[a], nums[b]);
    permSort(nums, a + 1);
    return;
}

int main()
{
    vector<int> n = {2, 3, 1};
    nextPermutation(n);
    for (int i : n)
    {
        cout << i << endl;
    }
}