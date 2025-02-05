#include <iostream>
#include <vector>

using namespace std;

void generate(vector<vector<int>> &res, vector<int> subres, int NumToFind, vector<int> &candidates, int idx);
vector<vector<int>> combinationSum(vector<int> &candidates, int target)
{
    vector<vector<int>> res;
    vector<int> sub;
    generate(res, sub, target, candidates, 0);
    return res;
}
void generate(vector<vector<int>> &res, vector<int> subres, int NumToFind, vector<int> &candidates, int idx)
{
    if (idx >= candidates.size())
    {
        return;
    }
    if (candidates[idx] == NumToFind)
    {
        subres.push_back(candidates[idx]);
        res.push_back(subres);
        subres.pop_back();
    }
    else if (NumToFind - candidates[idx] > 0)
    {
        subres.push_back(candidates[idx]);
        generate(res, subres, NumToFind - candidates[idx], candidates, idx);
        subres.erase(subres.end() - 1);
    }
    generate(res, subres, NumToFind, candidates, idx + 1);
}

int main()
{
    vector<int> r = {4, 2, 8};
    auto a = combinationSum(r, 8);
    for (vector<int> i : a)
    {
        for (int j : i)
        {
            cout << j;
        }
        cout << endl;
    }
}