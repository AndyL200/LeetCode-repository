class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        #use a BFS until all string states are seen
        q = deque([s])
        seen = set()
        smallest = s

        while q:
            cur = q.popleft()
            if cur in seen:
                continue
            seen.add(cur)
            
            if cur < smallest:
                smallest = cur
            
            #op1
            t = ""
            for i in range(len(cur)):
                if i % 2:
                    t += str((int(cur[i]) + a) % 10)
                else:
                    t += cur[i]
            q.append(t)
            #op2
            t = ""
            t = cur[-b:] + cur[:-b]
            q.append(t)

        return smallest