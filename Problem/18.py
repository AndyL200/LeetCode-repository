def fourSum(nums, target):
        nums.sort()
        res = []
        n = len(nums)
        for a in range(n):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            for b in range(a+1,n):
                if b > a+1 and nums[b] == nums[b-1]:
                    continue
                c = b + 1
                d = n - 1
                while c < d:
                    s = nums[a] + nums[b] + nums[c] + nums[d]
                    if s < target:
                        c+=1
                    elif s > target:
                        d-=1
                    else:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        c+=1
                        while c < d and nums[c] == nums[c-1]:
                            c+=1
        return res

print(fourSum([2,2,2,2,2], 8))