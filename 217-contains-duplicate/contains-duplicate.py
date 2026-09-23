class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        h=set()
        for i in nums:
            if i in h:
                return True
            h.add(i)
        return False

        