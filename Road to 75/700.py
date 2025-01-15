class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def searchBST(root: TreeNode, val: int) -> TreeNode:
        current = root
        q = []
        def dfs(start):
            
            if start:
                q.append(start.val)
                dfs(start.left)
                dfs(start.right)
            return q
        while current:
            if current.val < val:
                current = current.right
            elif current.val > val:
                current = current.left
            else:
                return dfs(current)

        return None

tll = TreeNode(1)
tlr = TreeNode(3)
tl = TreeNode(2, tll, tlr)
tr = TreeNode(7)
tree = TreeNode(4, tl, tr)

print(searchBST(tree, 2))