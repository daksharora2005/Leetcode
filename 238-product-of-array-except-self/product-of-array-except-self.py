class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total = 1
        zeroCount = 0
        for i in nums:
            if i==0:
                zeroCount += 1
            else:
                total *= i
        if zeroCount>1:
            result = [0*x for x in nums]
        elif zeroCount==1:
            result = [0 if x != 0 else total for x in nums]
        else:
            result = [total/x for x in nums]
        
        return result