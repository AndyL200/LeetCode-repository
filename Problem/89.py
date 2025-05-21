def log(x, base):
    if x <= 0:
        return -1
    if x == 1:
        return 0
    
    return 1 + log(x//base, base)
    

def grayCode(n: int):
    grey = [0]
    for i in range(1, 2**n):
        p = int(log(i, 2))
        ms = 1 if ((1 << p) & i) == (1 << p) else 0
        last = ms
        g = (1 << p) if ms else 0
        while p > 0:
            p-=1
            cur = 1 if ((1 << p) & i) == (1 << p) else 0
            if cur != last:
                g |= (1 << p)
            last = cur
        grey.append(g)
    return grey
            

print(grayCode(2))