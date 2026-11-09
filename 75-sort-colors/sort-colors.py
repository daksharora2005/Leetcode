class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        r=0
        w=0
        for i in nums:
            if i==0:
                r+=1
            elif i==1:
                w+=1
        b=r+w
        for i in range(len(nums)):
            if i<r:
                nums[i]=0
            elif i<b:
                nums[i]=1
            else:
                nums[i]=2