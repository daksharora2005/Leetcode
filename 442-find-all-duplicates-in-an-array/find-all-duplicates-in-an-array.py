class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        a=[]
        for i in range(len(nums)):
            value = abs(nums[i])
            index = value - 1
            if nums[index]<0:
                a.append(abs(nums[i]))
            else:
                nums[index]=nums[index]*-1
        return a        