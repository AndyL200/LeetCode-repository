def minimizeXor(self, num1: int, num2: int) -> int:
        k = bin(num2).count('1')
        
        x=0
        
        for i in range(31, -1, -1):
            if num1 & (1 << i) and k > 0:
                x |= (1 << i)
                k-=1
        for i in range(32):
            if k <= 0:
                break
            if not x & (1 << i):
                x |= (1 << i)
                k-=1
        return x    