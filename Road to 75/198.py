def rob(self, nums: List[int]) -> int:
    if len(nums) == 2:
        return max(nums[0], nums[1])
    elif len(nums) == 1:
        return nums[0]

    q = [nums[0], nums[1]]

    for i in range(2, len(nums)):
        m = q[i-2]
        for j in range(i-1):
            if q[j] > m:
                m = q[j]
        q.append(max(q[i-1], m + nums[i]))
    
    return q[-1]