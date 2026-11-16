class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left=0
        ml=float("inf")
        s=0
        for right in range(len(nums)):
            s+=nums[right]
            while s>=target:
                ml=min(ml,right-left+1)
                s-=nums[left]
                left+=1
        return ml if ml!=float("inf") else 0