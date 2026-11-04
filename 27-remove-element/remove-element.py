class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        n=len(nums)
        slow,fast=0,0
        while fast<n:
            if nums[slow]!=val:
                slow+=1
            elif nums[slow]==val and nums[fast]!=val:
                nums[slow],nums[fast]=nums[fast],nums[slow]
                slow+=1
            fast+=1
        return slow
        