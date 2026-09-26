class Solution(object):
    def evaluate(self, s, knowledge):
        """
        :type s: str
        :type knowledge: List[List[str]]
        :rtype: str
        """
        for i in knowledge:
            s=s.replace("("+i[0]+")",i[1])
        i=0
        while i<len(s):
            if s[i]=="(":
                j=s.find(")",i)
                s=s[:i] + "?" + s[j+1:]
            else:
                i+=1
        return s
            


        