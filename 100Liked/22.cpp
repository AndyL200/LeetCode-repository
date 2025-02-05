#include <iostream>
#include <vector>
#include <string>
using namespace std;
vector<string> generateParenthesis(int n)
{
    vector<string> res;
    generate(res, n, 0, 0, "");
    return res;
}

void generate(vector<string> &res, int n, int open, int closed, string path)
{
    if (open == closed == n)
    {
        res.push_back(path);
        return;
    }
    if (open < n)
    {
        generate(res, n, open + 1, closed, path + '(');
    }
    if (closed < open)
    {
        generate(res, n, open, closed + 1, path + ')');
    }
}