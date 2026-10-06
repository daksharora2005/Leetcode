class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l=0
        n=len(nums)
        while l<n:
            if nums[l]!=0:
                l+=1
                continue
            else:
                r=l+1
                while r<n:
                    if nums[r]!=0:
                        nums[l],nums[r]=nums[r],nums[l]
                        break
                    r+=1
                l+=1


        