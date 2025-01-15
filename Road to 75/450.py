class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def TreePrint(self, node):
        if node:
            print(node.val)
            self.TreePrint(node.left)
            self.TreePrint(node.right)

def deleteNode(root: TreeNode, key: int) -> TreeNode:
    current = root
    root_ref = root
    def minRight(node):
        while node.left.left:
            node = node.left
        value = node.left.val
        node.left = None
        return value
    while current:
        if current.val > key:
            current = current.left
        elif current.val < key:
            current = current.right
        else:
            current.val = minRight(current)
   
            
    return root_ref

tll = TreeNode(1)
tlr = TreeNode(3)
tl = TreeNode(2, tll, tlr)
tr = TreeNode(7)
tree = TreeNode(4, tl, tr)

tree = TreeNode()

deleteNode(tree, 0).TreePrint(deleteNode(tree, 0))