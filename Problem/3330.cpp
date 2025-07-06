#include <string>
#include <unordered_set>

int possibleStringCount(std::string word)
{
    int count = 0;
    std::unordered_set<char> w;
    w.insert(word[0]);
    for (int i = 1; i < word.size(); i++)
    {
        if (word[i] == word[i - 1] && w.find(word[i]) != w.end())
            count++;
        else
        {
            w.insert(word[i]);
        }
    }
    return count + 1;
}