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
       void search(TreeNode* node, vector<vector<int>>& vec, int depth) {
       
        if (vec.size() < depth) vec.push_back({});
        
       
        vec[depth - 1].push_back(node->val);
        
        if(node->left) search(node->left, vec, depth + 1);
        if(node->right) search(node->right, vec, depth + 1);
    }
    
    vector<vector<int>> levelOrderBottom(TreeNode* root) {
        
        vector<vector<int>> ans;
        if (root)search(root, ans, 1);
       
        
        std::reverse(ans.begin(), ans.end());
        return ans;
    }
};
