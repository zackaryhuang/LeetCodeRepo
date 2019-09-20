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
    bool isBalanced(TreeNode* root) {
        bool flag=true;
        Recursion(root,flag);
        return flag;
             
        
        
    }
    int Recursion(TreeNode* node, bool& flag){       
        if(node == NULL)
            return 0;
        else{        
            int l=Recursion(node->left,flag);
            int r=Recursion(node->right,flag);
            if(abs(l-r)>1)
                flag=false;
            return(1+max(l,r));
            
            
            
        }
        
    }
};
