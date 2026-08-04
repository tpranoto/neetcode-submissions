class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0

        l,r = 0, len(heights)-1
        max_area = 0
        while l<r:
            min_height = min(heights[l],heights[r])
            area = min_height * (r-l)
            max_area = max(max_area,area)

            if min_height == heights[l]:
                l+=1
            else:
                r-=1
        
        return max_area


        
        
        
        
        
        
        # if len(heights) == 0:
        #     return 0

        # l,r = 0,len(heights)-1
        # max_area = 0

        # while l < r:
        #     min_height = min(heights[l],heights[r])
        #     max_area = max(max_area,min_height * (r-l))
        #     if heights[l] < heights[r]:
        #         l +=1
        #     else:
        #         r -=1

        # return max_area
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
        # if len(heights) == 0:
        #     return 0

        # l = 0
        # r = len(heights)-1

        # max_amount = 0
        # while l < r:
        #     width = r - l
        #     curr_amount = width * min(heights[l],heights[r])
        #     max_amount = max(max_amount, curr_amount)
        #     if heights[l]<heights[r]:
        #         l+=1
        #     else:
        #         r-=1

        # return max_amount