def minWindow(s: str, t: str) -> str:
    fm_t = {}
    for c in t:
        if c in fm_t:
            fm_t[c] += 1
        else:
            fm_t[c] = 1
    

    small = s
    stack = []
    def comp(fm):
        for k in fm_t:
            if k not in fm or fm[k] < fm_t[k]:
                return False
        return True
    def dfs(i, fm):
        nonlocal small, stack
        if comp(fm):
            if len(stack) < len(small):
                small = "".join(stack)
        for j in range(i, len(s)):
            stack.append(s[j])
            if s[j] in fm:
                fm[s[j]] += 1
            else:
                fm[s[j]] = 1
            dfs(i+1,fm)
            fm[s[j]] -= 1
            stack.pop()

    dfs(0,{})

    return small

print(minWindow("ADOBECODEBANC", "ABC"))