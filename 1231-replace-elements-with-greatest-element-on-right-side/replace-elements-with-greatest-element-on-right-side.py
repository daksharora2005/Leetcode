class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        largest=float("-inf")
        for i in range(len(arr)-1,-1,-1):
            temp=arr[i] if arr[i]>largest else largest
            arr[i]=largest
            largest=temp
        arr[-1]=-1
        return arr
        