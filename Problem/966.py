def spellchecker(wordlist, queries):
    exact = set(wordlist)
    cases = {}
    vowels = {}
    def deVowel(w):
        build = ""
        for c in w:
            if c in 'aeiou':
                build += '*'
            else:
                build += c
        return build


    for w in wordlist:
        lower = w.lower()
        abstractVowels = deVowel(lower)
        if lower not in cases:
            cases[lower] = w
        if abstractVowels not in vowels:
            vowels[abstractVowels] = w
        
    result = []
        
    for q in queries:
        if q in exact:
            result.append(q)
        else:
            lower = q.lower()
            abstractVowels = deVowel(lower)
            if lower in cases:
                result.append(cases[lower])
            elif abstractVowels in vowels:
                result.append(vowels[abstractVowels])
            else:
                result.append("")
    return result
