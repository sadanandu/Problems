import time
class Solution:
    # https://www.interviewbit.com/problems/min-steps-in-infinite-grid/
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        points = [(x, y) for x, y in zip(A, B)]
        total = 0
        start = points[0]

        for each in points[1:]:
            starttime = time.clock()
            total += self.stepsBetween(start, each)
            start = each
            print 'time taken ', time.clock() - starttime

        return total

    def stepsBetween(self, p1, p2):
        steps = 0
        x1, y1 = p1
        x2, y2 = p2
        if x1 <> x2 and y1 <> y2:
            steps = min(abs(x2-x1), abs(y2-y1))
            if x1 < x2:
                x1 += steps
            elif x1 > x2:
                x1 -= steps
            if y1 < y2:
                y1 += steps
            elif y1 > y2:
                y1 -= steps




        if x1 <> x2:
            nowsteps = abs(x2- x1)
            steps += nowsteps
            if x1 < x2:
                x1 += nowsteps
            elif x1 > x2:
                x1 -= nowsteps

        if y1 <> y2:
            nowsteps = abs(y2- y1)
            steps += nowsteps
            if y1 < y2:
                y1 += nowsteps
            elif y1 > y2:
                y1 -= nowsteps
        return steps


s = Solution()
l1 = [2,3,4,5,6,7,8,9,10]
l2 = [-1,3,4,5,6,7,-2,-3, 5]
print s.coverPoints(l1, l2)