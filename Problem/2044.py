#brute force dfs solution
def countMaxOrSubsets_0(self, nums: List[int]) -> int:
    max_or = 0
    for n in nums:
        max_or |= n
    res = 0
    def dfs(i, cur_or):
        nonlocal max_or
        if i == len(nums):
            return 1 if cur_or == max_or else 0
        
        return dfs(i + 1, cur_or) + dfs(i+1, cur_or | nums[i])

    return dfs(0,0)

#2D matrix to cache to reduce the amount of repeated work (cuts time roughly in half)
def countMaxOrSubsets_1(self, nums: List[int]) -> int:
    max_or = 0
    for n in nums:
        max_or |= n
    
    cache = [[-1] * (max_or + 1) for _ in range(len(nums))]

    def dfs(i, cur_or):
        nonlocal max_or
        if i == len(nums):
            return 1 if cur_or == max_or else 0
        if cache[i][cur_or] != -1:
            return cache[i][cur_or]
        cache[i][cur_or] = dfs(i + 1, cur_or) + dfs(i+1, cur_or | nums[i])
        return cache[i][cur_or]

    return dfs(0,0)

#hashmap solution for memoization 
def countMaxOrSubsets_2(self, nums: List[int]) -> int:
    dp = defaultdict(int)
    dp[0] = 1
    max_or = 0
    for n in nums:
        new_dp = deepcopy(dp) #has to do with manipulating a data structure that you are currently looping through
        for cur_or, cnt in dp.items():
            new_or = n | cur_or
            new_dp[new_or] += cnt 

        dp = new_dp
        max_or |= n
    return dp[max_or]


#bitmasking solution
def countMaxOrSubsets_3(self, nums: List[int]) -> int:
    max_or = 0
    for n in nums:
        max_or |= n

    length = len(nums)
    res = 0

    for subset in range(1, 2**length):
        cur_or = 0
        for i in range(length):
           if (1 << i) & subset:
               cur_or |= nums[i]
        res += 1 if cur_or == max_or else 0
    return res