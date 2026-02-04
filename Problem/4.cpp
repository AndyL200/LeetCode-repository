#include <iostream>
#include <vector>
#include <unordered_map>
#include <cmath>

using namespace std;

    int indexSpace(unordered_map<int,pair<int,int>>& uset, int median, vector<int>& smaller, vector<int>& bigger, int i)
    {
        if(median <= -1 && uset.find(-1)!=uset.end())
        {
            //maybe add in edge case here
            return smaller[uset.at(-1).second - (median + 1)];
        }
        for(const auto& key : uset)
            {
                if (median > key.first && median < key.first + (uset.at(key.first).second - uset.at(key.first).first))
                {
                    
                    return smaller[uset.at(key.first).first + i];
                    break;
                }
            }
        return bigger[median];
    }
    int binarySearch(vector<int>& to, double val)
    {
        int high = to.size()-1, low = 0;
        int mid = low;
        while(low < high && to[mid] != val)
        {
            mid = (high + low)/2;
            if (val < to[mid])
            {
                high = mid;
            }
            else if(val > to[mid])
            {
                low = mid+1;
            }
            else {
                break;
            }
            
        }   
        if(low == 0 && to[mid] != val)
        return -1;
        else
        return mid;
    }
    int shiftingValues(vector<int>& to, double medianVal, int& median, double secondMedian, int start, int end) {

        //wont change if you only have one value
        if (start == end)
        {
            return binarySearch(to, secondMedian);
        }
        else if (start == end-1)
        {
            start = end;
            median = (secondMedian > medianVal)? median + 1: median - 1;
        }
        else {
        median = (secondMedian > medianVal)? median + ceil((end-start)/2): median - ceil((end-start)/2);
        }
        return binarySearch(to, secondMedian);
    }
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {

        //use set for indexing address spacing
        unordered_map<int, pair<int,int>> uset;

        vector<int>& bigger = (nums2.size() >= nums1.size())? nums2 : nums1;
        vector<int>& smaller = (nums2.size() < nums1.size())? nums2 : nums1;


            int median = bigger.size()/2;
            double medianVal = (bigger.size()%2 == 0)? (bigger[median] + bigger[median-1])/2.0: bigger[median];
            int start = 0;
            int end = smaller.size();
            int offset = 0;
            while(start < end)
            {
                double s_medianVal = ((start+end)%2 == 0)? (smaller[(start+end)/2] + smaller[((start+end)/2) - 1])/2.0: smaller[(start+end)/2]; 

                int insertion = shiftingValues(bigger, medianVal, median, s_medianVal, start, end);
                if (uset.find(insertion) == uset.end())
                uset[insertion] =  pair<int, int>{start, start+end/2};
                else
                {
                    uset.insert_or_assign(insertion, pair<int,int>{min(uset.at(insertion).first, start), max(uset.at(insertion).second, end)});
                }

                int i = abs(median - insertion);
                offset += (end-start)/2 + 1;
                
                if(insertion >= median)
                medianVal = ((bigger.size()+offset)%2 == 0)? (indexSpace(uset, median, smaller, bigger, i) + indexSpace(uset, median-1, smaller, bigger, i))/2.0: indexSpace(uset, median, smaller, bigger, i);
                else
                medianVal = ((bigger.size()+offset)%2 == 0)? (indexSpace(uset, median, smaller, bigger, i) + indexSpace(uset, median+1, smaller, bigger, i))/2.0: indexSpace(uset, median, smaller, bigger, i);

                start = (start + end)/2.0 + 1;
            }
        
        return medianVal;
    }

int main() {
    vector<int> a = {1,3};
    vector<int> b = {2};
    cout << findMedianSortedArrays(a, b);
    return 0;
}