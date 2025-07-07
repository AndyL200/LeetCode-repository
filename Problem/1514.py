import heapq
def maxProbability(n: int, edges, succProb, start_node, end_node) -> float:
    max_heap = []
    hm = {}
    for i, e in enumerate(edges):
        if e[0] not in hm:
            hm[e[0]] = {}
        if e[1] not in hm:
            hm[e[1]] = {}
        hm[e[0]][e[1]] = succProb[i]
        hm[e[1]][e[0]] = succProb[i]
    
    heapq.heappush(max_heap, (-1, start_node))
    visited = set()
    while max_heap:
        cur_prob, cur_node = heapq.heappop(max_heap)
        cur_prob *= -1
        if cur_node == end_node:
            return cur_prob
        if cur_node not in hm:
            continue
        for e in hm[cur_node]:
            if e not in visited:    
                heapq.heappush(max_heap, (-cur_prob * hm[cur_node][e], e) )
                visited.add(cur_node)
    return 0

        

print(maxProbability(n = 3, edges = [[0,1],[1,2],[0,2]], succProb = [0.5,0.5,0.3], start_node=0, end_node=2))