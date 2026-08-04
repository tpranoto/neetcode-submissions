class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if len(heights) == 0:
            return 0

        l = 0
        r = len(heights)-1

        max_amount = 0
        while l < r:
            width = r - l
            curr_amount = width * min(heights[l],heights[r])
            max_amount = max(max_amount, curr_amount)
            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1

        return max_amount