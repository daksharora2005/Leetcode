class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        left=0
        right=len(nums)-1
        s=0
        while left<right:
            s=nums[left]+nums[right]
            if s>target:
                right-=1
            elif s<target:
                left+=1
            else:
                return [left+1,right+1]
        