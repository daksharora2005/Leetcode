class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        nums.sort()
        i = 0
        while i <= len(nums) - 3:
            l = i + 1
            r = len(nums) - 1
            while l < r:
                current_sum = nums[i] + nums[l] + nums[r]
                if current_sum == 0:
                    res.add((nums[i], nums[l], nums[r]))
                    l+=1
                    r-=1
                elif current_sum<0:
                    l+=1
                else:
                    r-=1
            i+=1
        return [list(t) for t in res]

    