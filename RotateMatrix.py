#result[j][matrix.size() - i - 1] = matrix[i][j];
class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        for i in xrange(len(A)):
            for j in xrange(len(A[i])):
                temp = A[j][len(A)-i-1]
                A[j][len(A) - i - 1] = A[i][j]
                A[i][j] = temp
        return A

s = Solution()
print s.rotate([[1,2,3], [4,5,6], [7,8,9]                          ])