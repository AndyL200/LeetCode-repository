from collections import deque
def levelOrder(self, root):
    """
    :type root: Optional[TreeNode]
    :rtype: List[List[int]]
    """
    if not root:
        return []
    q = deque()
    q.append(root)
    res = []
    while q:
        r = []
        for _ in range(len(q)):
            curr = q.popleft()
            if curr:
                r.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
        res.append(r)
    return res