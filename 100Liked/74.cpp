#include <iostream>
#include <vector>
using namespace std;

int binarySearch(vector<int> n, int high, int low, int target)
{

    int mid = low + (high - low) / 2;

    if (low >= high)
    {
        return mid;
    }

    if (n[mid] < target)
    {
        return binarySearch(n, high, mid + 1, target);
    }
    else if (n[mid] > target)
    {
        return binarySearch(n, mid, low, target);
    }
    else
    {
        return mid;
    }
}
int binarySearch(vector<int> n, int target)
{
    return binarySearch(n, n.size() - 1, 0, target);
}
bool searchMatrix(vector<vector<int>> &matrix, int target)
{
    int col = matrix[0].size() - 1;
    int row = 0;
    vector<int> cols;
    while (row < matrix.size())
    {
        cols.push_back(matrix[row][col]);
        row++;
    }
    row = binarySearch(cols, target);
    int t = binarySearch(matrix[row], target);
    if (matrix[row][t] == target)
    {
        return true;
    }
    else
    {
        return false;
    }
}