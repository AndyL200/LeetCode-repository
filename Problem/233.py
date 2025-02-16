
def countDigitOne(n: int) -> int:
    def log(number):
        log_n = -1
        while number > 0:
            log_n += 1
            number//=10

        return log_n

    res = 0
    place = 0
    r = 0

    while n > 0:
        digit = n%10
        if digit != 0:
            if digit == 1:
                res += r
                log_digit = 0
            else:
                log_digit = place            
            S = 10**log_digit + (place*digit)*(10**(place-1))
            res += int(S)
        r += digit * 10**place
        n//=10
        place+=1
    return res
print(countDigitOne(3723))