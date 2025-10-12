int robhelp(vector<int>& nums)
    {
        int r1 = 0, r2 = 0;
        for(int n : nums)
        {
            int t = std::max(r1+n, r2);
            r1 = r2;
            r2 = t;
        }

        return r2;
    }
    int rob(vector<int>& nums) {
        if(nums.size() == 1){return nums[0];}
        vector<int> s1(nums.begin()+1, nums.end());
        vector<int> s2(nums.begin(), nums.end()-1);
        return std::max(
        robhelp(s1), 
        robhelp(s2)
        );
    }