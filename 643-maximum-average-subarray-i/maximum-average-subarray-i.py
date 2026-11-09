class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        l=0
        r=k-1
        n=len(nums)
        s=0
        for i in range(r+1):
            s+=nums[i]
        avg=s/k
        r+=1
        while r<n:
            s=s-nums[l]+nums[r]
            cur=s/k
            if cur>avg:
                avg=cur
            l+=1
            r+=1
        return avg
            
            