def tribonacci(n):
        """
        :type n: int
        :rtype: int
        """
        L = [0,1,1]
        i = 0
        for i in range(2,n):
            L.append(L[i]+L[i-1]+L[i-2])
        return L[len(L)-1]

print(tribonacci(30))