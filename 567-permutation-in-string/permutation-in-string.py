class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        d1={}
        for i in s1:
            if i not in d1:
                d1[i]=1
            else:
                d1[i]+=1
        d2={}
        n=len(s1)
        for i in range(n):
            if s2[i] in d2:
                d2[s2[i]]+=1
            else:
                d2[s2[i]]=1
        j=0
        while True:
            if d1==d2:
                return True
            elif n==len(s2):
                break
            else:
                d2[s2[j]]-=1
                if d2[s2[j]]==0:
                    del d2[s2[j]]
                if s2[n] in d2:
                    d2[s2[n]]+=1
                else:
                    d2[s2[n]]=1
                n+=1
                j+=1
        return False