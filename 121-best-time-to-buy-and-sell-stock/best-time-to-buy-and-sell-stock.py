class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0

        global_min = prices[0]
        global_max = prices[0]

        for price in prices:
            if price < global_min:
                global_min = price
            if price > global_max:
                global_max = price

        upper_bound = global_max - global_min

        lowest = prices[0]
        m = 0

        for price in prices:
            if price < lowest:
                lowest = price

            profit = price - lowest

            if profit > m:
                m = profit

                if m == upper_bound:
                    return m

        return m