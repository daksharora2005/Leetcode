class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s="".join(i for i in s if i.isalnum())
        s=s.lower()
        return True if s[::-1]==s else False


        