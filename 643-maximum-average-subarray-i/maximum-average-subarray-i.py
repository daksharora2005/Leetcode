class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        cur=sum(nums[:k])
        m=cur
        for i in range(k,len(nums)):
            cur+=nums[i]-nums[i-k]
            m=max(cur,m)
        return m/k
            
            