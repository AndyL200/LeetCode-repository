#include <vector>
#include <algorithm>

using namespace std;

class Solution
{
    public:
    size_t n;
    size_t g;

    void radixSort(vector<int>& temp, int b = 10)
    {
        int maxDigits = 0;
        int maxVal = *max_element(temp.begin(), temp.end());
        while(maxVal > 0)
        {
            maxVal /= 10;
            maxDigits++;
        }
        vector<vector<int>> chamber(b);


        for(int p = 0; p < maxDigits; ++p)
        {
            long unsigned int u = 10;
            for(int x = 0; x < p; ++x)
            {
                u *= b;
            }
        for(int i = 0; i < temp.size(); ++i)
        {
           
            int digit = (temp[i] % u) / (u/10);
            chamber[digit].push_back(temp[i]);
        }
        temp.clear();
        
        for(int i = 0; i < chamber.size(); ++i)
        {
            temp.insert(temp.end(), chamber[i].begin(), chamber[i].end());
            chamber[i].clear();
        }
        }
    }

    vector<vector<int>> diagonalSort(vector<vector<int>>& mat) {
        n = mat[0].size();
        g = mat.size();   
        int j = 0;
        vector<int> temp;
        for(int i = 0; i < g; ++i)
        {
            int y = i;
            int x = 0;
            int c = 0;
            while(x + c < n && y + c < g)
            {
                temp.push_back(mat[y + c][x + c]);
                c++;
            }
            radixSort(temp);
            for(int j = 0; j < c; ++j)
            {
                mat[y+j][x+j] = temp[j];
            }
            temp.clear();
        }
        for(int i = 0; i < n; ++i)
        {
            int y = 0;
            int x = i;
            int c = 0;
            while(x + c < n && y + c < g)
            {
                temp.push_back(mat[y + c][x + c]);
                c++;
            }
            radixSort(temp);
            for(int j = 0; j < c; ++j)
            {
                mat[y+j][x+j] = temp[j];
            }
            temp.clear();
        }

        return mat;
    }
};