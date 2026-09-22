class Solution(object):
    def maxProfit(self, prices):
        max_profit=0
        max_price=0
        while prices:
            price=prices.pop()

            if price>max_price:
                max_price=price
            else:
                max_profit=max(max_profit,max_price-price)
        return max_profit