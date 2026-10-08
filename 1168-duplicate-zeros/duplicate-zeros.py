class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i=0
        l=len(arr)
        while i<l:
            if arr[i]==0:
                arr.pop()
                arr.insert(i+1,0)
                i+=2
            else:
                i+=1   

        