class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l=0
        m=0
        r=len(height)-1
        while l<r:
            area=0
            if height[l]==height[r]:
                area=(r-l)*height[l]
                if m<area:
                    m=area
                if height[l+1]>height[r-1]:
                    l+=1
                elif height[l+1]<height[r-1]:
                    r-=1
                else:
                    l+=1
                    r-=1
            elif height[l]<height[r]:
                area=(r-l)*height[l]
                if m<area:
                    m=area
                l+=1
            else:
                area=(r-l)*height[r]
                if m<area:
                    m=area
                r-=1
        return m
            
        