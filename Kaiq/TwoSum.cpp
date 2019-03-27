class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
        vector<int> index;
        int len = nums.size();
        for(int i=0;i<len;i++){
            for(int j=i+1;j<len;j++){
                if(nums[i]==target-nums[j]){
                    index.push_back(i);
                    index.push_back(j);
                    return index;
                }
            }            
        }
    return index;          
    }
};
