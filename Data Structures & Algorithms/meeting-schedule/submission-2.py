"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 0:
            return True
            
        intervals.sort(key=lambda i: i.start)

        output = [intervals[0]]

        for i in intervals[1:]:
            last_end = output[-1].end

            if i.start < last_end:
                return False
            else:
                output.append(Interval(i.start,i.end))

        return True