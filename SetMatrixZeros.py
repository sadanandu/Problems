class Solution:
    # https://www.interviewbit.com/problems/set-matrix-zeros/
    # @param A : list of list of integers
    # @return the same list modified
+
    def set_row_col(self, row, col, A):
        '''try:
            A[row].index(1)
            now_col = col -1
            while now_col >= 0:
                A[row][now_col] = 0
                now_col -= 1
            now_col = col + 1
            while now_col < len(A[row]):
                A[row][now_col] = 0
                now_col += 1
        except ValueError:
            pass'''

        #A[row] = [0 for each in xrange(len(A[row]))]
        now_row = row -1
        while now_row >= 0:
            A[now_row][col] = 0
            now_row -= 1
        now_row = row + 1
        while now_row < len(A):
            A[now_row][col] = 0
            now_row += 1

s = Solution()
print s.setZeroes([ [0,1,1], [1,1,1], [1,1,0]])
print s.setZeroes([ [0,0], [1,1]])
print s.setZeroes([ [0,0], [1,0]])





