class Solution(object):
    def maxProfit(self, prices):
        mp=float('inf')
        mx=0
        for price in prices:
            if price<mp:
                mp=price
            elif price-mp>mx:
                mx=price-mp    
        return mx