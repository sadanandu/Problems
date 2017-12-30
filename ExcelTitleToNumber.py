class Solution:
    # https://www.interviewbit.com/problems/excel-column-number/
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        d = {'a': 1, 'c': 3, 'b': 2, 'e': 5, 'd': 4, 'g': 7, 'f': 6, 'i': 9, 'h': 8, 'k': 11, 'j': 10, 'm': 13, 'l': 12,
         'o': 15, 'n': 14, 'q': 17, 'p': 16, 's': 19, 'r': 18, 'u': 21, 't': 20, 'w': 23, 'v': 22, 'y': 25, 'x': 24,
         'z': 26}
        power = 0
        number = 0
        for each in reversed(A.lower()):
            number += d[each]*26**power
            power += 1
        return number

s = Solution()
print s.titleToNumber('Z')
print s.titleToNumber('AA')
print s.titleToNumber('BA')
print s.titleToNumber('AAA')

