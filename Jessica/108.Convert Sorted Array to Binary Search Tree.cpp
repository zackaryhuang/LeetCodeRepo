/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
//每次都是取中间
class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return convertToBst(nums, 0, nums.size()-1);
        
    }
    
TreeNode* convertToBst(vector<int>& nums, int begin, int end)
{
    if (begin > end)
        return NULL;
    
    if (begin == end)
    {
        return new TreeNode(nums[begin]);
    }
    int mid = (begin + end)/2;
    TreeNode* root = new TreeNode(nums[mid]);
    root->left = convertToBst(nums,begin, mid-1 );
    root->right = convertToBst(nums,mid+1, end);
    return root;
        
    }
    
};
