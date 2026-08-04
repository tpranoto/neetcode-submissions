class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ms = []
        max_area = 0

        for i, h in enumerate(heights):
            start_idx = i

            while len(ms)!=0 and ms[-1][1] > h:
                curr_i,curr_h = ms.pop()
                max_area = max(max_area, (curr_h*(i-curr_i)))
                start_idx = curr_i

            ms.append((start_idx,h))

        for i,h in ms:
            max_area = max(max_area,h*((len(heights))-i))
        
        
        return max_area
        
        
        # for i, h in enumerate(heights):
        #     start_idx = i
        #     while len(ms) != 0 and ms[-1][1] > h:
        #         s_idx,s_h = ms.pop()
        #         max_area = max(max_area,(i-s_idx)*s_h)
        #         start_idx = s_idx

        #     ms.append((start_idx,h))

        # for i,h in ms:
        #     max_area = max(max_area, (len(heights)-i) *h)
        
        # return max_area



