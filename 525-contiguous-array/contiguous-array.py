class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        bal={0:-1}
        b=0
        m=0
        for i,ch in enumerate(nums):
            if ch==0:
                b-=1
            else:
                b+=1
            if b in bal:
                l=i-bal[b]
                if l>m:
                    m=l
            else:
                bal[b]=i
        return m