def minCostClimbingStairs(self, cost):
    """
    :type cost: List[int]
    :rtype: int
    """
    sums = [0] * (len(cost)+1)
    sums[0] = cost[0]
    sums[1] = cost[1]
    for i in range(2, len(cost)):
        sums[i] = cost[i] + min(sums[i-1], sums[i-2])

    sums[-1] = min(sums[-2], sums[-3])
    return sums[-1]