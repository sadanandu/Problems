# Definition for an interval.
# https://www.interviewbit.com/problems/merge-overlapping-intervals/
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
import itertools
class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        # sort intervals
        # starts = [each_interval.start for each_interval in intervals]
        result = []
        len_at_start = len(intervals)
        while True:
            len_at_start = len(intervals)
            for i in xrange(len(intervals)):
                int1 = intervals[i]
                intervals_to_merge = [int1]
                for j in xrange(i + 1, len(intervals)):
                    int2 = intervals[j]
                    # int1 starts from within int2
                    if int2.start <= int1.start <= int2.end or int1.start <= int2.start <= int1.end:
                        intervals_to_merge.append(int2)
                if len(intervals_to_merge) > 1:
                    intervals.append(self.merge_intervals(intervals_to_merge))
                    for each in intervals_to_merge:
                        intervals.remove(each)
                    break
            if len_at_start == len(intervals):
                break
            '''int1 = intervals[0]
            intervals_to_merge= [int1]
            found_overlap = False
            for i in xrange(1, len(intervals)):
                int2 = intervals[i]
                #int1 starts from within int2
                if int2.start <= int1.start <= int2.end or int1.start <= int2.start <=int1.end:
                    intervals_to_merge.append(int2)
            if len(intervals_to_merge) >1:
                found_overlap = True
            for each in intervals_to_merge:
                intervals.remove(each)
            intervals.append(self.merge_intervals(intervals_to_merge))'''

            '''# int1 inside int2
                    if int1.end <= int2.end:
                        result.append(int2)
                    else:
                        result.append(Interval(int2.start, int1.end))
                    merged = True
                #int2 starts from within int1
                if int1.start <= int2.start <=int1.end:
                    #int2 inside int1
                    if int2.end <= int1.end:
                        result.append(int1)
                    else:
                        result.append(Interval(int1.start, int2.end))
                    merged = True'''



        '''for i in xrange(len(intervals)):
            int1 = intervals[i]
            merged = False
            for j in xrange(i+1, len(intervals)):
                int2 = intervals[j]
                #int1 starts from within int2
                if int2.start <= int1.start <= int2.end:
                    # int1 inside int2
                    if int1.end <= int2.end:
                        result.append(int2)
                    else:
                        result.append(Interval(int2.start, int1.end))
                    merged = True
                #int2 starts from within int1
                if int1.start <= int2.start <=int1.end:
                    #int2 inside int1
                    if int2.end <= int1.end:
                        result.append(int1)
                    else:
                        result.append(Interval(int1.start, int2.end))
                    merged = True
            if not merged:
                result.append(int1)'''



        return sorted(intervals, key=lambda x: x.start)
                    #self.merge_intervals(int1, int2)

                #int2 starts from int1


    def merge_intervals(self, intervals):
        start = float('inf')
        end = 0
        for each in intervals:
            if each.start < start:
                start = each.start
            if each.end > end:
                end = each.end
        return Interval(start, end)
        '''if int1.start < int2.start:
            return Interval(int1.start, int2.end)
        else:
            return Interval(int2.start, int1.end)'''



s = Solution()
res = s.merge([Interval(1,5), Interval(3, 6), Interval(8,10), Interval(2,4), Interval(15,18), Interval(9,17)])
print 'result is'
for each in res:
    print each.start, each.end
res = s.merge([Interval(1,5), Interval(8,10), Interval(15,18)])
print 'result is'
for each in res:
    print each.start, each.end


