def maxProduct(nums) -> int:
    res = [nums[0]] * len(nums)
    for i in range(len(nums)-2, -1, -1):
        res[i] = max(nums[i] * res[i+1], nums[i], nums[i] * nums[i+1])
    return max(res)

print(maxProduct([2,3,-2,4]))