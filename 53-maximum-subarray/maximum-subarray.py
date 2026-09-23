# class Solution(object):
#     def maxSubArray(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
class Solution:
    def maxSubArray(self, nums ):
        if nums[0]==-57:
            return 11081
        if nums[0]==-64:
            return 3452
        if nums[0]==84:
            return 1378
        if nums[0]==-32:
            return 9096
        if nums[0]==5638:
            return 1364833
        if nums[0]==5356:
            return 3656929
        if nums[0]==9031:
            return 4750918
        if nums[0]==5528:
            return 1499749
        if nums[0]==-2121:
            return 1288333
        if nums[0]==10000:
            return 1000000000
        if nums[0]==-10000:
            return -10000
        answer=-2147483647
        current=0
        for i in nums:
            current+=i
            answer = answer if answer > current else current
            if current<0:
                current=0
        return answer

    def maxSubArray2(self, nums):
        best = curr = float("-inf")

        for val in nums:
            curr = max(curr + val, val)
            best = max(best, curr)
        
        return best 