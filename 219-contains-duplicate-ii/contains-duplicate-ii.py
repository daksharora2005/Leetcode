class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        s = set()
        n = len(nums)
        for i in range(n):
            if nums[i] in s:
                return True
            s.add(nums[i])
            if len(s) > k:
                s.discard(nums[i - k])
        return False
