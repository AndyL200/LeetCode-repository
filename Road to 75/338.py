def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    L = [0]*(n+1)
    
    for i in range(1,n+1):
        L[i] = L[i >> 1] + (i & 1)

    return L

print(countBits(30))

#DYNAMIC