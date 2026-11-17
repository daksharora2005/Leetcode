class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        if n==0:
            return 0
        ss=set()
        z=0
        for i in s:
            if i not in ss:
                z+=1
                ss.add(i)
            else:
                break 
        window=[s[0]]
        l=1
        ml=1
        for i in range(1,n):
            if s[i] not in window:
                window.append(s[i])
                l+=1
            else:
                stop=False
                for j in range(l-1,0,-1):
                    if window[j]==s[i]:
                        while j!=0:
                            stop=True
                            window.pop(j)
                            l-=1
                            j-=1
                        if stop:
                            break
                window.append(s[i])
                l+=1
            ml=max(l,ml)
        return max(ml-1,z)