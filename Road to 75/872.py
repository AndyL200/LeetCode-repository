def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    q = []
    s = []
    def dfs(start, arr):
        if start:
            if start.left or start.right:
                dfs(start.left, arr)
                dfs(start.right, arr)
            else:
                arr.append(start.val)

    dfs(root1, q)
    dfs(root2, s)
    if q == s:
        return True
    return False