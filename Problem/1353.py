import queue
def maxEvents(events) -> int:
    pq = queue.PriorityQueue()
    events.sort(key=lambda x: x[1]-x[0])
    for e in events:
        pq.put((e[1], e))
    d = 0
    c = 0
    visited = set()
    while not pq.empty():
        p, cur = pq.get()
        d = max(d, cur[0])
        if cur[0] <= d <= cur[1] and (cur[0] not in visited or cur[1] not in visited):
            if d < cur[1]:
                visited.add(cur[0])
                d = cur[0] + 1
            elif d == cur[1]:
                visited.add(cur[1])
                d = cur[1] + 1
            #NOOOO
            c += 1

    return c

print(maxEvents([[1,2],[2,2],[3,3],[3,4],[3,4]]))