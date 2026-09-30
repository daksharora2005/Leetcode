class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        largest=float("-inf")
        for i in range(len(arr)-1,-1,-1):
            if largest<arr[i]:
                temp=largest
                largest=arr[i]
                arr[i]=temp
                continue
            arr[i]=largest
        arr[-1]=-1
        return arr
        