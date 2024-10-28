import math

def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
       
        res = 0
        sign = True
        keys = ['0','1','2','3','4','5','6','7','8','9']
        mapping = {key:idx for idx, key in enumerate(keys)}

        
        s = s.strip()
        if len(s) == 0:
            return 0
        if s[0] == '-':
            sign = False
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        for i in range(len(s)):
            if s[i] in mapping:
                res = res * 10 + mapping.get(s[i])
            else:
                break
        
        if math.fabs(res) >= int(2**31-1) and sign:
            return int(2**31-1)
        elif math.fabs(res) >= int(2**31):
            return int(-2**31)
        return res if sign else -res