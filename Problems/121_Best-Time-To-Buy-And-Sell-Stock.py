# Time complexity: O(n)
# Space complexity: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0

        for price in prices:
            if(minPrice > price):
                minPrice = price
            if(maxProfit < (price - minPrice)):
                maxProfit = (price - minPrice)
        
        return maxProfit