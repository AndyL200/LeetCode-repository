def sortVowels(self, s: str) -> str:
    q1 = []
    q2 = []
    t = []
    def is_vowel(char):
        if char.lower() in 'aeiou':
            return True
        return False
    for i, v in enumerate(s):
        if is_vowel(v):
            q1.append(i)
            q2.append(v)
        t.append(v)

    q2.sort()
    for i, v in enumerate(q1):
        t[v] = q2[i]
    
    return ''.join(t)