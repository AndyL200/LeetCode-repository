def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()


        for a in range(len(nums)):
            if a > 0 and nums[a] == nums[a-1]:
                continue
            l = a + 1
            r = len(nums)-1
            
            while l < r:
                s = nums[a] + nums[l] + nums[r]
                
                if s < 0:
                    l+=1
                elif s > 0:
                    r-=1
                else:
                    res.append([nums[a], nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
        return res