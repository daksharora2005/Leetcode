class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        n=len(nums)
        f=0
        s=0
        while f<n:
            if nums[s]!=nums[f]:
                s+=1
                nums[s]=nums[f]
            f+=1
        return s+1
        