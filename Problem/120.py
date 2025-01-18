def minimumTotal(self, triangle):
    """
    :type triangle: List[List[int]]
    :rtype: int
    """
    n = len(triangle)
    minsum = triangle[-1]
    layer = n-2
    while layer >= 0:
        for i in range(layer+1):
            minsum[i] = min(minsum[i], minsum[i+1]) + triangle[layer][i]
        layer-=1
    return minsum[0]