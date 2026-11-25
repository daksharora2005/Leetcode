class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        check=""
        check=s1[-1::-1]
        d1={}
        for i in check:
            if i not in d1:
                d1[i]=0
            else:
                d1[i]+=1
        d2={}
        n=len(s1)
        i=0
        while n<=len(s2):
            d2={}
            check2=s2[i:n]
            for j in check2:
                if j not in d2:
                    d2[j]=0
                else:
                    d2[j]+=1
            if d2==d1:
                return True
            else:
                i+=1
                n+=1
        return False