def integerBreak(n: int) -> int:
    if n == 1 or n == 0:
        return 1

    dp = []
    for i in range(n):
        dp.append(i)
    dp.append(1)

    for i in range(2, n+1):
        for j in range(1, i):
            dp[i] = max(dp[i], dp[i-j]*dp[j])

    return dp[n]