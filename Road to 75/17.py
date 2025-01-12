
def letterCombinations(digits: str) -> List[str]:
    d = {
    2: ['a','b','c'],
    3: ['d','e','f'],
    4: ['g','h','i'],
    5: ['j','k','l'],
    6: ['m','n','o'],
    7: ['p','q','r','s'],
    8: ['t','u','v'],
    9: ['w','x','y','z']
    }
    combos = []
    def dfs(build, idx):
        if idx < len(digits):
            for i in d[int(digits[idx])]:
                dfs(build + i, idx+1)
        else:
            if build:
                combos.append(build)
    dfs("", 0)
    return combos