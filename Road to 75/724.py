def pivotIndex(nums):
    leftMost = 0
    rightMost = 0
    for j in range(len(nums)):
        rightMost += nums[j]
    for i in range(len(nums)):
        leftMost += nums[i-1] if i != 0 else leftMost
        rightMost -= nums[i]
        if leftMost == rightMost:
            break
        i = -1
    return i

print(pivotIndex([2,1,-1]))