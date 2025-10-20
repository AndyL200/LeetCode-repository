import collections
class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        best = 0

        for b in range(n):
            f = collections.Counter()
            submax = 0
            count = 0
            for e in range(b, n):
                f[s[e]] += 1
                #ensuring same frequency
                submax = max(submax, f[s[e]])
                count+=1
                if submax * len(f) == count:
                    best = max(best, count)
        return best
            