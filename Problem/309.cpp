int rec(vector<int>& prices, bool b, int idx, vector<vector<int>>& cache)
    {
        if(idx >= prices.size())
        {
            return 0;
        }
        if(cache[(int)b][idx] != 0)
        {
            return cache[(int)b][idx];
        }
       
        int cooldown = rec(prices, b, idx+1, cache);
        if(b)
        {
            //buy
            int buy = rec(prices, !b, idx+1, cache) - prices[idx];
            cache[(int)b][idx] = std::max(buy, cooldown);
        }
        else
        {
            //selling
            int sell = rec(prices, !b, idx+2, cache) + prices[idx];
            cache[(int)b][idx] = std::max(sell, cooldown);
        }

        return cache[(int)b][idx];

    }
    int maxProfit(vector<int>& prices) {
        vector<vector<int>> cache = vector<vector<int>>(2, vector<int>(prices.size(), 0));
       return rec(prices, true, 0, cache);
    }