class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        s=set()
        n=len(nums)
        if k>n:
            k=n
        for i in range(k):
            if nums[i] in s:
                return True
            else:
                s.add(nums[i])
        for i in range(k,n):
            if nums[i] in s:
                return True
            else:
                s.add(nums[i])
                s.discard(nums[i-k])
        return False 