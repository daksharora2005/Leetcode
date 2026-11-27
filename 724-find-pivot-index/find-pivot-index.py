class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total=sum(nums)
        left_s=0
        for i,cur in enumerate(nums):
            right_s=total-left_s-cur
            if left_s==right_s:
                return i
            left_s+=cur
        return -1
        
