import queue
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        q = queue.PriorityQueue()
        hm = {}
        for time in times:
            if time[0] not in hm:
                hm[time[0]] = {}
            hm[time[0]][time[1]] = time[2]
        visited = [False] * (n+1)

        res = 0
        q.put((0,k))
        while not q.empty():
            curDist, curNode = q.get()
            if visited[curNode]:
                continue
            visited[curNode] = True
            res = curDist
            n-=1
            if curNode in hm:
                for nxt in hm[curNode]:
                    q.put((curDist + hm[curNode][nxt], nxt))

        return res if n == 0 else -1
    


import queue
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)
        for u, v, w in times:
            edges[u].append((v,w))
        
        minHeap = [(0,k)]
        visit = set() #track visited nodes
        t = 0 #track max traversal value

        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visit:
                continue
            visit.add(n1)
            t = w1
            for n2, w2 in edges[n1]:
                if n2 not in visit:
                    heapq.heappush(minHeap, (w2 + w1, n2))
        
        return t if len(visit) == n else -1