from collections import deque
class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n=len(s)
        se=deque(s[:3])
        if len(set(se))==3:
            count=1
        else:
            count=0
        for i in range (3,n):
            se.popleft()
            se.append(s[i])
            if len(set(se))==3:
                count+=1
        return count

        