def minDeletionSize(self, strs: List[str]) -> int:
    res = 0

    for i in range(0, len(strs[0])):
        for j in range(1, len(strs)):
            if strs[j][i] < strs[j-1][i]:
                res += 1
                break
            # elif strs[i][j] > strs[i-1][j]:
            #     break
    return res