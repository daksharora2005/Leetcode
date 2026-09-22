class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        st=0
        en=len(s)-1
        while st<en:
            if not s[st].isalnum():
                st+=1
                continue
            if not s[en].isalnum():
                en-=1
                continue
            if s[st].lower()!=s[en].lower():
                return False 
            st+=1
            en-=1
        return True


        