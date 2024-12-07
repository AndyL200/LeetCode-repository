

 
class J104 {
    
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;        this.left = left;
            this.right = right;
        }
     }
    public int maxDepth(TreeNode root) {
        if(root == null) {return 0;}
        else if(root.left == null && root.right == null) {return 1;}
        int i = 1;
        return maxDepth(root, i);
    }
    public int maxDepth(TreeNode current, int depth) {
        if(current == null) {return depth-1;}
        //if(current.left != null || current.right != null) {
        else {
            depth = Math.max(maxDepth(current.left, depth+1),maxDepth(current.right,depth+1));
        }
        return depth;
        }
}