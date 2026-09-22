class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        m = 0
        lowest=prices[0]
        for p in prices:
            if p<lowest:
                lowest=p
            elif m<p-lowest:
                m=p-lowest
        return m

