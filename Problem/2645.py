#DP problem but solved using a regular grammar and finite automata

def addMinimum(word: str) -> int:
    s_a = s_b = s_c = False

    a = 'a'
    b = 'b'
    c = 'c'

    total = 0
    if len(word) == 0:
        return 0
    elif len(word) == 1:
        return 2

    if word[0] == a:
        s_a = True
    elif word[0] == b:
        total += 1
        s_b = True
    elif word[0] == c:
        total += 2
        s_c = True
    else:
        return 0

        
    for i in range(1, len(word)):
        if s_a:
            if word[i] == a:
                total+=2
            elif word[i] == b:
                s_a = False
                s_b = True
            else:
                total+=1
                s_a = False
                s_c = True
        elif s_b:
            if word[i] == a:
                total+=1
                s_a = True
                s_b = False
            elif word[i] == b:
                total+=2
            else:
                s_c = True
                s_b = False
        elif s_c:
            if word[i] == a:
                s_a = True
                s_c = False
            elif word[i] == b:
                total += 1
                s_b = True
                s_c = False
            else:
                total+=2
    
    
    if s_a:
        total+=2
    elif s_b:
        total+=1

    return total
