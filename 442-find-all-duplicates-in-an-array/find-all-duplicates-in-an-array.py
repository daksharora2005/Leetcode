class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        s=[]
        dic=set()
        for i in nums:
            if i not in dic:
                dic.add(i)
            else:
                s.append(i)
        return s
        