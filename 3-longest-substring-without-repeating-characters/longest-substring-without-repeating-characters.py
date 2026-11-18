class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        ml=0
        d={}
        for right in range(len(s)):
            char=s[right]
            if char in d and d[char]>=left:
                left=d[char]+1
            d[char]=right
            ml=max(ml,right-left+1)
        return ml
