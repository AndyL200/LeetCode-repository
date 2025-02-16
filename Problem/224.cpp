// recode for understanding
#include <iostream>
#include <string>
#include <stack>
using namespace std;

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
        return -1;
    }
}
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
int calculate(string s)
{
    int cur = 0, res = 0, sign = 1;

    stack<int> state;

    for (char c : s)
    {
        if (isdigit(c))
        {
            cur = cur * 10 + todigit(c);
        }
        else if (c == '+' || c == '-')
        {
            res += cur * sign;

            sign = (c == '+') ? 1 : -1;
            cur = 0;
        }
        else if (c == '(')
        {
            state.push(res);
            state.push(sign);
            res = 0;
            sign = 1;
        }
        else if (c == ')')
        {
            res += cur * sign;
            sign = state.top();
            state.pop();
            res += sign * state.top();
            state.pop();
            cur = 0;
        }
    }
    return res + cur * sign;
}