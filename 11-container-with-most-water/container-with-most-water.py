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
            b=r-l
            hl=height[l]
            hr=height[r]
            if hl==hr:
                area=b*hl
                if m<area:
                    m=area
                if height[l+1]>height[r-1]:
                    l+=1
                elif height[l+1]<height[r-1]:
                    r-=1
                else:
                    l+=1
                    r-=1
            elif hl<hr:
                area=b*hl
                if m<area:
                    m=area
                l+=1
            else:
                area=b*hr
                if m<area:
                    m=area
                r-=1
        return m
            
        