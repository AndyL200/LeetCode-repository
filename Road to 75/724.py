def pivotIndex(nums):
    
    for i in range(len(nums)):
        leftMost = 0
        rightMost = 0
        for j in range(0, i):
            leftMost += nums[j]
        for j in range(i+1, len(nums)):
            rightMost += nums[j]
        if leftMost == rightMost:
            break
        i = -1
    return i

print(pivotIndex([1,7,3,6,5,6]))