def maxProduct(nums) -> int:
    res = max(nums)
    cMin, cMax = 1, 1

    for n in nums:
        if n == 0:
            cMin, cMax = 1,1
            continue
        temp = cMax
        cMax = max(n*cMax, n * cMin, n)
        cMin = min(n*temp, n * cMin, n)
        if cMax > res:
            res = cMax
    return res