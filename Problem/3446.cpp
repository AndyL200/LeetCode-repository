#include <vector>
#include <algorithm>
using namespace std;

class Solution {
    public:
    size_t n;
    size_t g;
void findDiagonal(vector<vector<int>>& grid, int x, int y)
{
    vector<int> acc;
    int c = 0;
    while(y + c < g && x + c < n && y >= 0 && x >= 0)
    {
        acc.push_back(grid[y + c][x + c]);
        ++c;
    }
    
        sort(acc.begin(), acc.end());
        for(int i = 0; i < c; ++i)
        {
            grid[y + i][x + i] = acc[c - i - 1];
        }
}
void findDiagonalTop(vector<vector<int>>& grid, int x, int y)
{
    vector<int> acc;
    int c = 0;
    while(y + c < g && x + c < n && y >= 0 && x >= 0)
    {
        acc.push_back(grid[y + c][x + c]);
        ++c;
    }
    
        sort(acc.begin(), acc.end());
        for(int i = 0; i < c; ++i)
        {
            grid[y + i][x + i] = acc[i];
        }
}
vector<vector<int>> sortMatrix(vector<vector<int>>& grid) {
    n = grid[0].size();
    g = grid.size();
    //bottom
    for(int i = 0; i < g; ++i)
    {
        findDiagonal(grid, 0, i);
    }
    //top
    for(int i = 1; i < n; ++i)
    {
        findDiagonalTop(grid, i, 0);
    }

    return grid;
}
};