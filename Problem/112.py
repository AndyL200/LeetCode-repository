def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False
    def dfs(r, acc):
        if r.left == None and r.right == None:
            if acc == targetSum:
                return True
            else:
                return False
        elif r.left and r.right:
            return dfs(r.left, acc + r.left.val) or dfs(r.right, acc + r.right.val)
        elif r.left:
            return dfs(r.left, acc + r.left.val)
        else:
            return dfs(r.right, acc + r.right.val)
    return dfs(root, root.val)