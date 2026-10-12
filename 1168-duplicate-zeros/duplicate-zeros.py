class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        n=len(arr)
        z=0
        l=0
        while l<n-z:
            if arr[l]==0:
                if l==n-1-z:
                    arr[n-1]=0
                    n-=1
                    break
                z+=1
            l+=1
        r=l-1
        w=n-1
        while r>=0:
            if arr[r]==0:
                arr[w]=0
                arr[w-1]=0
                w-=2
            else:
                arr[w]=arr[r]
                w-=1
            r-=1