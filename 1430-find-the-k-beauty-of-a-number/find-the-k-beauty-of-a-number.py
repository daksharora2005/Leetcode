class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s=str(num)
        beauty=0
        x=""
        for i in range(k):
            x+=s[i]
        if num%int(x)==0:
            beauty+=1
        for i in range(k,len(s)):
            x=x[1:]+s[i]
            divisor=int(x)
            if divisor>0:
                if num%divisor==0:
                    beauty+=1
        return beauty
        