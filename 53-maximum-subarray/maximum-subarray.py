class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=nums[0]
        gsum=nums[0]
        for i in nums[1:]:
            s=max(i,s+i)
            if s>gsum:
                gsum=s
        return gsum





        