class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        nums.sort()
        return [nums[x] for x in range(len(nums)-1) if nums[x]==nums[x+1]]

        