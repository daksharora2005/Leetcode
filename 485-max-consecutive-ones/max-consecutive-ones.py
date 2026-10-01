class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        m=0
        cur=0
        for i in nums:
            if i==1:
                cur+=1
                if m<cur:
                    m=cur
            else:
                cur=0
        return m