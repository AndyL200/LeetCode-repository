def restoreIpAddresses(s: str):
    res = []
    cur = []

    def dfs(i):
        nonlocal cur, res
        if i == len(s) and len(cur) == 4:
            res.append('.'.join(cur))
            return
        if len(cur) == 4:
            return
        
        for j in range(i, i+3):
            if j < len(s):
                digit = s[i:j+1]
                if digit[0] == '0' and len(digit) > 1:
                    continue
                if int(digit) >= 0 and int(digit) <= 255:
                    cur.append(digit)
                    dfs(j+1)
                    cur.pop()
    dfs(0)
    return res
