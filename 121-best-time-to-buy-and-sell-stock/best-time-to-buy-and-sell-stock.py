class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                max_profit = max(max_profit, profit)
        
        return max_profit

        x=min(prices)
        minp=prices[0]
        imin=0
        for i in range(len(arr)):
            if prices[i]<minp:
                minp=prices[0]
                imin=i
        l=prices[imin:]
        maxp=l[0]
        for i  in range(len(l)):
            if l[i]>maxp:
                maxp=l[i]
        return maxp-minp
