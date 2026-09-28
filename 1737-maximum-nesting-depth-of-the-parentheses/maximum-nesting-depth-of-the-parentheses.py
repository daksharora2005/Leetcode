class Solution:
    def maxDepth(self, s: str) -> int:
        md=0
        cd=0
        for char in s:
            if char=='(':
                cd+=1
                md=max(md,cd)
            elif char==')':
                cd-=1
        return md 
        