class Solution{
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> record;
        for(int i = 0; i < nums.size(); i++)
        {
            int num2find = target - nums[i];
            if(record.find(num2find) != record.end())
            {
                return vector<int>(i + 1, record[num2find] + 1);
            }
            record[nums[i]] = i;
        }
    }
};
