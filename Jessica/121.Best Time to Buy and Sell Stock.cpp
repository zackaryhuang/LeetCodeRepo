class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.size()<2){
            return 0;
        }
        int low = prices[0];
        int MaxProfit=0;
        for(int i=1;i<prices.size();i++){
            if (prices[i]>low){
                MaxProfit=max(MaxProfit,prices[i]-low);                
            }
            else{
                low=min(low,prices[i]);
            }
        }
        
        return MaxProfit;
    }
};
