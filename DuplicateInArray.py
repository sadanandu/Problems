class Solution:
    # https://www.interviewbit.com/problems/find-duplicate-in-array/
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        hash_table = {}
        for each in A:
            if each not in hash_table:
                hash_table[each] = 1
            else:
                return each
        return -1

