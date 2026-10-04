class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n=len(nums)-1
        l=set()
        for i in range(n+1):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            left,right=i+1,n
            while left<right:
                s=nums[left]+nums[right]
                if s==-nums[i]:
                    l.add((nums[left],nums[right],nums[i]))
                    left+=1
                elif s<-nums[i]:
                    left+=1
                else:
                    right-=1
        return [i for i in l]

