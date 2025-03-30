def subsets(nums):
    res = []
    sub = []

    def dfs(start):
        res.append(sub.copy())
        for i in range(start, len(nums)):
            sub.append(nums[i])
            dfs(i+1)
            sub.pop()
    dfs(0)
    return res