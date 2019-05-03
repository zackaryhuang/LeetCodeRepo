/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    bool isSymmetric(TreeNode* root) {
        return Recursion(root,root);
        
    }
    bool Recursion(TreeNode* n1,TreeNode* n2){
        if(n1==NULL && n2==NULL)
            return true;
        else if (n1==NULL || n2==NULL)
            return false;
        else{
            if(n1->val != n2->val)
                return false;
            else{
                return (Recursion(n1->left, n2->right) && (Recursion(n1->right, n2->left)));
            }
        }
    }
};
