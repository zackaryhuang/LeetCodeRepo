class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<2:
            return 0
        MinP = prices[0]
        MaxProfit=0
        for i in range(1,len(prices)):
            if prices[i] > MinP:
                MaxProfit=max(MaxProfit,prices[i] - MinP)
            else:
                MinP=min(MinP,prices[i])
                
        return MaxProfit
        
           
