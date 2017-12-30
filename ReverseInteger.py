class Solution:
    # https://www.interviewbit.com/problems/reverse-integer/
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        sign = ''
        if str(A).startswith('-'):
            sign = '-'
            A = int(str(A)[1:])
        #print sign, A
        rev = ''.join(reversed(str(A)))
        #print 'rev ', rev
        rev_int = int(sign+rev)
        if abs(rev_int) > (2**31 -1):
            return 0
        return rev_int

s = Solution()
print s.reverse(123)
print s.reverse(-123)
print s.reverse(123567893)
print s.reverse(-1153072433)