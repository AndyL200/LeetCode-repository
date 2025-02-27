#include <iostream>
#include <vector>

using namespace std;

int partition(vector<int> &input, int high, int low, int mid)
{

    // makeshift median of thirds
    if (input[low] > input[mid])
    {
        swap(input[low], input[mid]);
    }
    if (input[high] < input[low])
    {
        swap(input[high], input[low]);
    }
    if (input[mid] > input[high])
    {
        swap(input[mid], input[high]);
    }

    // move pivot to end of the array
    int pivot = input[mid];

    swap(input[high], input[mid]);

    int i = low - 1;

    for (int j = low; j <= high - 1; j++)
    {
        if (input[j] < pivot)
        {
            i++;
            swap(input[i], input[j]);
        }
    }
    swap(input[i + 1], input[high]);

    return i + 1;
}

void quick_sort(vector<int> &input, int low, int high)
{
    int mid = low + (high - low) / 2;

    if (low < high)
    {
        int p = partition(input, high, low, mid);
        quick_sort(input, p + 1, high);
        quick_sort(input, low, p - 1);
    }
}
void quick_sort(vector<int> &input)
{
    quick_sort(input, 0, input.size() - 1);
}
int threeSumClosest(vector<int> &nums, int target)
{
    quick_sort(nums);

    for (int i : nums)
    {
        cout << i << endl;
    }
    int n = nums.size();
    int mi = nums[0] + nums[1] + nums[2];
    for (int a = 0; a < n; a++)
    {
        int l = a + 1;
        int r = n - 1;
        while (l < r)
        {
            int s = nums[a] + nums[l] + nums[r];
            if (s < target)
            {
                l++;
            }
            else if (s > target)
            {
                r--;
            }
            else
            {
                return s;
            }
            if (abs(target - s) < abs(target - mi))
            {
                mi = s;
                l++;
            }
        }
    }
    return mi;
}

int main()
{
    vector<int> r = {-84, 92, 26, 19, -7, 9, 42, -51, 8, 30, -100, -13, -38};
    cout << threeSumClosest(r, 1);
}