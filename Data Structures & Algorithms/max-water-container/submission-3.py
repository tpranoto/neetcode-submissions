class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0,len(heights)-1

        area = 0

        while l<=r:
            h = min(heights[l],heights[r])
            area = max(area, h* (r-l))

            if h == heights[l]:
                l+=1
            else:
                r-=1
        
        return area