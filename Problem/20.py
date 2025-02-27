def isValid(self, s: str) -> bool:
    stack = []
    for i in range(len(s)-1, -1, -1):
        if s[i] == '(':
            if stack:
                if stack.pop() != ')':
                    return False
            else:
                return False
        elif s[i] == '[':
            if stack:
                if stack.pop() != ']':
                    return False
            else:
                return False
        elif s[i] == '{':
            if stack:
                if stack.pop() != '}':
                    return False
            else:
                return False
        elif s[i] == ')' or s[i] == '}' or s[i] == ']':
            stack.append(s[i])
    if len(stack) > 0:
        return False
    return True