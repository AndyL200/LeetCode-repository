def kthCharacter(k, operations):
        
    def rec(val, acc):
        jump = 0
        while (1 << jump) < val:
            jump+=1
        if acc > 26:
            acc %= 26
        if val <= 1:
            return chr(ord('a') + acc)
        return rec(val - (1 << (jump-1)), acc + operations[jump-1])
    
    return rec(k, 0)

print(kthCharacter(10, [0,1,0,1]))