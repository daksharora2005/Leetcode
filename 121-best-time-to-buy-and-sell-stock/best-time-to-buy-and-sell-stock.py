class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        upper_bound=max(prices)-min(prices)
        lowest=prices[0]
        m=0
        for price in prices:
            lowest=min(lowest, price)
            profit=price-lowest
            m=max(m,profit)
            if m==upper_bound:
                return m

        return m



            

