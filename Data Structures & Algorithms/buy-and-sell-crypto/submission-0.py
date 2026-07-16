class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        minprice=prices[0]
        for i in range(len(prices)):
            currprice = prices[i] - minprice
            if currprice > profit:
                profit = currprice
            minprice = min(minprice, prices[i])    
        return profit