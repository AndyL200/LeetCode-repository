class Solution(object):
    def divide(self, dividend, divisor):
        Innercount = 1
        Outercount = 0
        orgDiv = abs(divisor)
        truthyDivend = False if dividend < 0 else True
        truthyDivsor = False if divisor < 0 else True
        dividend = abs(dividend)
        divisor = abs(divisor)
        while divisor < dividend:
            pastDiv = divisor
            pastCount = Innercount
            divisor += divisor
            Innercount += Innercount
            if divisor > dividend:
                dividend -= pastDiv
                divisor = orgDiv
                Outercount += pastCount
                Innercount = 1

        dividend -= divisor
        Outercount = Outercount + Innercount if dividend == 0 else Outercount

        if Outercount > 2147483647 and truthyDivend == truthyDivsor:
            return 2147483647
        elif Outercount > 2147483648 and truthyDivend != truthyDivsor:
            return -2147483648
        else:
            if truthyDivend == truthyDivsor:
                return Outercount
            else:
                return -Outercount
