def isNumber(s: str) -> bool:
    s = s.strip()

    point = False
    eSeen = False
    intSeen = False
    afterE = False

    for i in range(len(s)):
        if ord('0') <= ord(s[i]) and ord('9') >= ord(s[i]):
            intSeen = True
            afterE = True
        elif s[i] == '.':
            if eSeen or point:
                return False
            point = True
        elif s[i].lower() == 'e':
            if eSeen or not intSeen:
                return False
            afterE = False
            eSeen = True
        elif s[i] == '-' or s[i] == '+':
            if i != 0 and s[i-1].lower() != 'e':
                return False
        else:
            return False
    return intSeen and afterE