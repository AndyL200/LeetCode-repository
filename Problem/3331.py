import collections
def findSubtreeSizes(parent, s: str):
    N = len(s)
    sn = [ord(c) - ord('a') for c in s]
    children = collections.defaultdict(set)

    for i, p in enumerate(parent):
        if p != -1:
            children[p].add(i)
    
    def rec(node, parent, last_seen):
        if last_seen[sn[node]] is not None:
            children[parent].remove(node)
            children[last_seen[sn[node]]].add(node)
        
        prev = last_seen[sn[node]]
        last_seen[sn[node]] = node

        cs = list(children[node])
        #children[node] is subject to change but cs will stay constant, fulfilling the simultaneous requirement
        for c in cs:
            rec(c, node, last_seen)
        last_seen[sn[node]] = prev
    rec(0, -1, [None]*26)
    ans = [1] * N
    def rec2(node):
        for c in children[node]:
            ans[node] += rec2(c)
        return ans[node]
    rec2(0)
    return ans

