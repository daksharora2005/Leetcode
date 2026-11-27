class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        sumLeft=[nums[0]]
        total=sum(nums)
        n=len(nums)
        for i in range(1,n):
            sumLeft.append(sumLeft[i-1]+nums[i])
        for i in range(n):
            if i==0:
                left_s=0
            else:
                left_s=sumLeft[i-1]
            if i==n-1:
                right_s=0
            else:
                right_s=total-left_s-nums[i]
            if left_s==right_s:
                return i
        return -1
        
