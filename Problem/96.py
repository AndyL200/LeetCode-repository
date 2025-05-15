def numTrees(n: int) -> int:
    if n == 0:
        return 1
    elif n == 1:
        return 1
    
    ans = [1] * (n + 1)

    s = 0
    for i in range(1, n):
        if not ans[i-1]:
            ans[i-1] = numTrees(i-1)
        if not ans[n-i]:
            numTrees(n-i)
        s += ans[i-1] * ans[n-i] 

    return s



print(numTrees(4))