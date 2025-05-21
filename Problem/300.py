def lengthOfLIS(nums) -> int:
    
    sub = []

    for i in range(len(nums)):
        if not sub or nums[i] > sub[len(sub)-1]:
            sub.append(nums[i])
        else:
            l = 0
            h = len(sub)-1
            m = (l + h) // 2
            while l < h:
                m = (l + h) // 2
                if sub[m] < nums[i]:
                    l = m + 1
                else:
                    h = m
            sub[l] = nums[i]

    return len(sub)