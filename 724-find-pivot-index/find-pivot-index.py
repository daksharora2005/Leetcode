class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total=sum(nums)
        left_s=0
        for i in range(len(nums)):
            right_s=total-left_s-nums[i]
            if left_s==right_s:
                return i
            left_s+=nums[i]
        return -1
        
