class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int Sum=0;
        int Max_Num=nums[0];
        for(int i=0;i<nums.size();i++){
            Sum+=nums[i];
            Max_Num=max(Max_Num,Sum);
            Sum=max(Sum,0);
        }
        return Max_Num;
    }
};
