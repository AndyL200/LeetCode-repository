def numDecodings(self, s: str) -> int:     
    n = len(s)
    if n == 0 or s[0] == '0':
        return 0

    ans = [0] * (n)
    ans.append(1)

    for i in range(n-1,-1,-1):
        if s[i] == '0':
            ans[i] = 0
        elif i+1 >= n:
            ans[i] = 1
        elif int(s[i] + s[i+1]) <= 26:
            ans[i] = ans[i+1] + ans[i+2]

        else:
            ans[i] = ans[i+1]

    return ans[0]