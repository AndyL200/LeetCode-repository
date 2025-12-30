/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {

    int max_depth = 0;
    public boolean dfs(TreeNode root, int acc) {
        
        max_depth = max(max_depth, acc);
        if (root == null) {
            if (abs(max_depth - acc) >= 2) {
                return false;
            }
        }
        else {
            dfs(root.left, acc+1);
            dfs(root.right, acc+1);
        }
        return true;
    }
    public boolean isBalanced(TreeNode root) {
        return dfs(root, 0);
    }
}