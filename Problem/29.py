
def divide(dividend, divisor):
    count = 1
    orgDiv = divisor
    orgDivend = dividend
    truthyDivend = False if dividend < 0 else True
    truthyDivsor = False if divisor < 0 else True
    dividend = abs(dividend)
    divisor = abs(divisor)
    while dividend > 0:
        dividend = dividend - divisor
        divisor = divisor + divisor
        count = count + count

    count = count - divide(abs(dividend), abs(orgDiv)) if abs(orgDivend) > abs(dividend) else count
    
    if(truthyDivend == truthyDivsor):
        return count
    else:
        return -count

print(divide(1000,10))