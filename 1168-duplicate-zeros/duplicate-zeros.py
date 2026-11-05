class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        n=len(arr)
        x=n
        for i in range(n):
            if arr[i]==0:
                x+=1
        if x!=n:
            fast=n-1
            slow=x-1
            while fast>=0:
                if arr[fast]!=0:
                    if slow<n:
                        arr[slow]=arr[fast]
                    slow-=1
                else:
                    if slow<n:
                        arr[slow]=0
                    slow-=1
                    if slow<n:
                        arr[slow]=0
                    slow-=1
                fast-=1



