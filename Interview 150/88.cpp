#include <iostream>
#include <vector>

class Solution {
    Solution() {

    }
    ~Solution() {
        delete this;
    }
public:
    void merge(std::vector<int>& nums1, int m, std::vector<int>& nums2, int n) {
        for(int i = 0; i < m; i++) {
            nums1.insert(nums2.end(),nums2.at(i));
        }
        std::cout << "finished" << std::endl;
        
    }

    void main() {
    Solution hire;
    std::vector<int> x = {1,2,3,0,0};
    std::vector<int> y = {4,5};
    hire.merge(x, x.size(),y, y.size());

}

};
