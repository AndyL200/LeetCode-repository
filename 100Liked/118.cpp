#include <iostream>
#include <vector>

using namespace std;

class Solution
{
public:
    vector<vector<int>> generate(int numRows)
    {
        vector<vector<int>> pTri;
        vector<int> first = {1};
        pTri.push_back(first);
        numRows--;

        while (numRows > 0)
        {
            vector<int> row;
            vector<int> last = pTri.back();
            row.push_back(1);
            for (int i = 1; i < last.size(); i++)
            {
                int x = last[i - 1] + last[i];
                row.push_back(x);
            }
            row.push_back(1);
            pTri.push_back(row);
            numRows--;
        }
        return pTri;
    }
};