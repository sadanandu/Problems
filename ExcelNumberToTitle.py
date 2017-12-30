class Solution:
    # https://www.interviewbit.com/problems/excel-column-title/
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        d =  {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e', 5: 'f', 6: 'g', 7: 'h', 8: 'i', 9: 'j', 10: 'k', 11: 'l', 12: 'm', 13: 'n', 14: 'o', 15: 'p', 16: 'q', 17: 'r', 18: 's', 19: 't', 20: 'u', 21: 'v', 22: 'w', 23: 'x', 24: 'y', 25: 'z'}

        op = []
        num = A
        rem = 0

        ind = 0
        while num >26 :
            rem, ind = num%26, int(num/26)
            if ind in d:
                op.append(d[ind])
            num = ind

        '''while maxpow > 0:
            op.append(d[26])
            maxpow -= 1'''
        if num:
            op.append(d[num])
        if rem:
            op.append(d[rem])
        return ''.join(op)


s = Solution()
print s.convertToTitle(25)
print s.convertToTitle(27)
print s.convertToTitle(52)


