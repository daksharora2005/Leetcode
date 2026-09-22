class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m = 0
        lowest=prices[0]
        for p in prices:
            lowest=min(p,lowest)
            m=max(m,p-lowest)
        return m

