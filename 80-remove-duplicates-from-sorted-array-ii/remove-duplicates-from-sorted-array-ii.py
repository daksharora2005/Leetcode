class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        slow=0
        fast=1
        while fast<len(nums):
            if nums[slow]==nums[fast]:
                slow+=1
                fast+=1
                while fast<len(nums) and nums[fast]==nums[slow]:
                    nums.pop(fast)
                slow=fast
                fast=fast+1
            else:
                slow+=1
                fast+=1
        return len(nums)
