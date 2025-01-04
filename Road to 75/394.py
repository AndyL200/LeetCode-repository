def decodeString(self, s: str) -> str:
    stack = []
    for i in range(len(s)):
        
        if s[i] == ']':
            sub = ""
            it_er = stack.pop()
            while(it_er != '['):
                sub = it_er + sub
                it_er = stack.pop()
            num = stack.pop()
            while stack and stack[-1].isdigit():
                num = stack.pop() + num
            n = int(num)
            while n > 0:
                stack.append(sub)
                n-=1
        else:
            stack.append(s[i])
    
    return ''.join(stack)

print(decodeString("100[leetcode]"))