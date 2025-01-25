#include <array>
#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

class Solution1
{
public:
    bool subCheck(vector<vector<char>> board, int row)
    {
        for (int z = 0; z < 3; z++)
        {
            unordered_set<char> grid;
            for (int i = row - 2; i <= row; i++)
            {
                for (int j = 3 * z; j < 3 * z + 3; j++)
                {
                    if (!grid.count(board[i][j]) && board[i][j] != '.')
                    {
                        grid.insert(board[i][j]);
                    }
                    else if (board[i][j] == '.')
                    {
                        continue;
                    }
                    else
                    {
                        return false;
                    }
                }
            }
        }
        return true;
    }
    bool isValidSudoku(vector<vector<char>> &board)
    {
        vector<unordered_set<char>> rows = vector<unordered_set<char>>(9);
        for (int i = 0; i < 9; i++)
        {
            unordered_set<char> cols;
            if (i % 3 == 2)
            {
                bool sub = subCheck(board, i);
                if (!sub)
                    return false;
            }
            for (int j = 0; j < 9; j++)
            {
                if (!cols.count(board[i][j]) && board[i][j] != '.')
                {
                    cols.insert(board[i][j]);
                    if (!rows[j].count(board[i][j]))
                    {
                        rows[j].insert(board[i][j]);
                    }
                    else
                    {
                        return false;
                    }
                }
                else if (board[i][j] == '.')
                {
                    continue;
                }
                else
                {
                    return false;
                }
            }
        }
        return true;
    }
};
// This solution is much faster using bitmasking (super cool and super elegant solution)
class Solution2
{
public:
    bool isValidSudoku(vector<vector<char>> &board)
    {
        for (int r = 0; r < 9; r++)
        {

            int row = 0;
            int col = 0;
            int box = 0;

            for (int c = 0; c < 9; c++)
            {
                int i = (r % 3) * 3 + (c % 3); // Think of it as rewriting the subgrids to 1D arrays
                int j = (r / 3) * 3 + (c / 3);
                if (board[r][c] != '.')
                {
                    int rowBit = 1 << ((int)board[r][c] - '0');
                    if (row & rowBit)
                        return false;
                    row |= rowBit;
                }

                if (board[c][r] != '.')
                {
                    int colBit = 1 << ((int)board[c][r] - '0');
                    if (col & colBit)
                        return false;
                    col |= colBit;
                }

                if (board[j][i] != '.')
                {
                    int boxBit = 1 << ((int)board[j][i] - '0');
                    if (box & boxBit)
                        return false;
                    box |= boxBit;
                }
            }
        }
        return true;
    }
};