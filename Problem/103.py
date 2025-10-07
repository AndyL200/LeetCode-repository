from collections import deque
def zigzagLevelOrder(root):
    if not root:
        return []
    cur = root
    res = []
    q = deque([root])
    d = False
    while q:
        t = []
        if d:
            for c in range(len(q)):
                cur = q.pop()
                t.append(cur.val)


                if cur.right:
                    q.appendleft(cur.right)
                if cur.left:
                    q.appendleft(cur.left)
                

        else:
            for c in range(len(q)):
                cur = q.popleft()
                t.append(cur.val)

                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
        d = not d
        res.append(t)
    
    return res

