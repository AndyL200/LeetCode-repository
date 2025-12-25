def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
    happiness.sort(reverse=True)
    res = 0
    for i in range(k):
        cur = happiness[i] - i
        if cur > 0:
            res += cur
        else:
            break
    return res