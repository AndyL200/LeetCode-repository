def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
    sub = text.split(' ')

    count = 0
    for w in sub:
        for c in w:
            if c in brokenLetters:
                count-=1
                break
        count+= 1
    return count