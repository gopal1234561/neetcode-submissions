"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=self.get_start)
        for i in range(1,len(intervals)):
            if intervals[i].start<intervals[i-1].end:
                return False
        return True
    def get_start(self,interval):
        return interval.start
