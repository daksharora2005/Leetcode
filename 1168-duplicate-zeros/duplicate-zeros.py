class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        arr2=[]
        l=len(arr)
        for i in arr:
            if i!=0:
                arr2.append(i)
            else:
                arr2.extend([0,0])
        arr[:]=arr2[:l]