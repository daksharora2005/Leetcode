class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        s=0
        n=len(nums)
        for f in range(n):
            if nums[f]%2==0 and nums[s]%2!=0:
                nums[s],nums[f]=nums[f],nums[s]
                s+=1
            elif nums[f]%2==0:
                s+=1
        return nums
        