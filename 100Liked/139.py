def wordBreak(s: str, wordDict) -> bool:
    m = 0
    for w in wordDict:
        if len(w) > m:
            m = len(w)
    q = [s]
    while q:
        for _ in range(len(q)):
            cur = q.pop(0)
            i = 0
            while i <= m:
                if cur[:i] in wordDict:
                    if cur[i:len(cur)] not in q:
                        q.append(cur[i:len(cur)])
                if cur == "":
                    return True
                i+=1
    return False




print(wordBreak("applepenapple", ['apple', 'pen']))
