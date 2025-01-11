def isSubsequence(self, s: str, t: str) -> bool:
    if len(s) == 0:
        return True
    c = 0
    for i in range(len(t)):
        if t[i] == s[c]:
            c+=1
        if c == len(s):
            break
    if c == len(s):
        return True
    else:
        return False