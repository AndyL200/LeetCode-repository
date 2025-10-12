#include <iostream>
#include <vector>

using std::vector;

int candy(vector<int>& ratings) {
        if(ratings.size() == 0)
        {
            return 0;
        }
        vector<int> children(ratings.size(), 1);
        for(int i = 0; i < ratings.size(); ++i)
        {
            children[i] += (i+1 < ratings.size() && ratings[i] > ratings[i+1])? abs(children[i] - children[i+1]) + 1 : 0;
            children[i] += (i-1 >= 0 && ratings[i] > ratings[i-1])? abs(children[i] - children[i-1]) + 1 : 0;
        }
        int res = 0;
        for(int i = 0; i < children.size(); ++i)
        {
            res += children[i];
        }

        return res;

       
    }

int main() {
    vector<int> rate = {1,0,2};
    std::cout << candy(rate) << std::endl;
}