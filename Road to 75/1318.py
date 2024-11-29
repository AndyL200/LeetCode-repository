
def minFlips(self, a, b, c):
    """
    :type a: int
    :type b: int
    :type c: int
    :rtype: int
    """
    count = 0
    temp = a|b
    res = temp^c
    while res > 0:
        if res & 1:
            if a & 1 and b & 1:
                count+=1
            count+=1    
        res >>= 1
        a >>= 1
        b >>= 1

    return count
    