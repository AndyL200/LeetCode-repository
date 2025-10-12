class Solution {
public:
    vector<string> splitStrings(string& sentence, char del)
    {
        string word = "";
        vector<string> res;
        for(int i = 0; i < sentence.length(); ++i)
        {
            if (sentence[i] == del)
            {
                res.push_back(word);
                word = "";
                while(sentence[i] == del)
                {
                    i += 1;
                }
                i-=1;
            }
            else
            {
                word += sentence[i];
            }
        }
        if (!word.empty())
        {
            res.push_back(word);
        }
        return res;
        
    }
    int compareVersion(string version1, string version2) {
        vector<string> v1 = splitStrings(version1, '.');
        vector<string> v2 = splitStrings(version2, '.');

        size_t len = (v2.size()>v1.size())? v2.size() : v1.size();
        for(int i = 0; i < len; ++i)
        {
            string v1_rev;
            string v2_rev;
            if(i >= v1.size() && i >= v2.size())
            {
                return 0;
            }
            else if(i >= v1.size())
            {
                v1_rev = "0";
                v2_rev = v2[i];
            }
            else if(i >= v2.size())
            {
                v2_rev = "0";
                v1_rev = v1[i];
            }
            else
            {
                v1_rev = v1[i];
                v2_rev = v2[i];
            }
            int val1 = stoi(v1_rev);
            int val2 = stoi(v2_rev);
            if(val1 > val2)
            {
                return 1;
            }
            else if(val1 < val2)
            {
                return -1;
            }
        }
        return 0;
    }
};