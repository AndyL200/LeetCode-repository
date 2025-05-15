def permute(nums):
    res = [nums]
    def per(arr, idx):
        if idx <= 0:
            return
        for i in range(idx):
            c = arr.copy()
            c[i], c[idx] = c[idx], c[i]
            per(c, idx-1)
            res.append(c)
        per(arr,idx-1)
    per(nums, len(nums)-1)
    return res

print(permute([1,2,3]))