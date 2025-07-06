#include <iostream>
#include <vector>

int acc = 0;
static const long long i = 1;
char kthCharacter(long long k, std::vector<int> &operations)
{
    if (k <= 1)
    {
        return (char)((int)'a' + acc % 26);
    }
    int jump = 0;
    // ceil log2k
    while ((i << jump) < k)
    {
        ++jump;
    }
    acc += operations[jump - 1];
    return kthCharacter(k - (i << (jump - 1)), operations);
}