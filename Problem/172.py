def trailingZeroes(n) -> int:
    n5 = 0
    m5 = 5
    while(n >= m5):
        n5 += n/m5
        m5 *= 5
    return int(n5)
print(trailingZeroes(25))