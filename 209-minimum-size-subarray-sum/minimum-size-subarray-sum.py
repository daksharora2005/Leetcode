class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left=0
        ml=float("inf")
        s=0
        f=False
        for right in range(len(nums)):
            s+=nums[right]
            while s>=target:
                x=right-left+1
                if ml>x:
                    ml=x
                    f=True
                s-=nums[left]
                left+=1
        return ml if f else 0