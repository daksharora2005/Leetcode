class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_p=prices[0]
        mp=0
        for i in range(1,len(prices)):
            if prices[i]>min_p:
                mp+=prices[i]-min_p
                min_p=prices[i]
            min_p=prices[i]
        return mp

            


        