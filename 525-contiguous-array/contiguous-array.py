class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        bal={0:-1}
        b=0
        m=0
        for i in range(len(nums)):
            if nums[i]==0:
                b-=1
            else:
                b+=1
            if b not in bal:
                bal[b]=i
            else:
                m=max(m,i-bal[b])
        return m