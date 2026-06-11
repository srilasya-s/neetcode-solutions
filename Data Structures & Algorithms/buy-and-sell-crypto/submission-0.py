class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        min_price = prices[0]
        
        for i in range (len(prices)):
            Profit = prices[i]- min_price
            res = max(res, Profit)
            min_price = min(min_price,prices[i])
            
        return res 
                

