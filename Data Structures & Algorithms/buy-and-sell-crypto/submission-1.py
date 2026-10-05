class Solution:
    def maxProfit(self, prices: List[int]) -> int:        
        profit = [0]
        for i in range(len(prices)):
            for j in range(0,i):
                if prices[i]-prices[j]>0:
                    profit.append(prices[i]-prices[j])
        return max(profit)

        