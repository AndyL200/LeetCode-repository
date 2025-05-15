def maxProfit(self, prices: List[int]) -> int:
    profit = 0
    for j in range(1, len(prices)):
        if prices[j] > prices[j-1]:
            profit += prices[j] - prices[j-1]
    return profit