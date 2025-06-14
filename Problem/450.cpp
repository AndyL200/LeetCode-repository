/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
    public:
        TreeNode* deleteNode(TreeNode* root, int key) {
            TreeNode* current = root;
            TreeNode* parent = nullptr;
            while(current && current->val != key) {
                parent = current;
                if(key > current->val) {
                    current = current->right;
                }
                else if(key < current->val) {
                    current = current->left;
                }
            }
            if(!current) {
                return root;
            }
            //Option 1: Both children 
            if(current->left && current->right) {
                TreeNode* cur = current->right;
                TreeNode* par = current;
                while(cur->left) {
                    par = cur;
                    cur = cur->left;
                }
                current->val = cur->val; 
                if(par->left == cur) {
                    par->left = cur->right;
                }
                else {
                    par->right = cur->right;
                }
                return root;
            }
            //sub edge case if not parent only one child
            if(!parent) {
                TreeNode* child = (current->left)? current->left:current->right;
                root = child;
                return root;
            }
    
    
            bool isLeft = (parent->left == current);
            //Option 2: One child
            if(current->left || current->right) {
                TreeNode* child = (current->left)? current->left:current->right;
                if(isLeft) {
                    parent->left = child;
                }
                else {
                    parent->right = child;
                }
            }
            //Option 3: No children
            else {
                if(isLeft) {
                    parent->left = nullptr;
                }
                else {
                    parent->right = nullptr;
                }
            }
        return root;
    
        }
    };