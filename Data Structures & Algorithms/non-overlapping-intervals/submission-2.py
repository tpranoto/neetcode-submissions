class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        output = [intervals[0]]

        count = 0
        for start, end in intervals[1:]:
            last_end = output[-1][1]

            if start < last_end:
                count+=1
            else:
                output.append([start, end])

            
        return count