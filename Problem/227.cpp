#include <iostream>
#include <string>

using namespace std;

bool isdigit(char c)
{
    switch (c)
    {
    case '0':
    case '1':
    case '2':
    case '3':
    case '4':
    case '5':
    case '6':
    case '7':
    case '8':
    case '9':
        return true;
    default:
        return false;
    }
}
void applyOperation(int &res, int &cur, int &prev, char &operation)
{
    if (operation == '+')
    {
        res += cur;
        prev = cur;
    }
    else if (operation == '-')
    {
        res -= cur;
        prev = -cur;
    }
    else if (operation == '*')
    {
        res -= prev;
        res += cur * prev;
        prev = cur * prev;
    }
    else
    {
        res -= prev;
        res += prev / cur;
        prev = prev / cur;
    }
}
int todigit(char c)
{
    switch (c)
    {
    case '0':
        return 0;
    case '1':
        return 1;
    case '2':
        return 2;
    case '3':
        return 3;
    case '4':
        return 4;
    case '5':
        return 5;
    case '6':
        return 6;
    case '7':
        return 7;
    case '8':
        return 8;
    case '9':
        return 9;
    default:
        break;
    }
    return -1;
}
int calculate(string s)
{
    int cur = 0, prev = 0, res = 0;

    char cur_operation = '+';

    int i = 0;
    while (i < s.size())
    {
        char cur_char = s[i];

        if (isdigit(cur_char))
        {
            while (i < s.size() && isdigit(s[i]))
            {
                cur = cur * 10 + todigit(s[i]);
                i++;
            }
            i--;
            applyOperation(res, cur, prev, cur_operation);
            cur = 0;
        }
        else if (cur_char != ' ')
        {
            cur_operation = cur_char;
        }
        i++;
    }

    return res;
}