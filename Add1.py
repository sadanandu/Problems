class Solution:
    # https://www.interviewbit.com/problems/add-one-to-number/
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        carry = 0
        answer = []
        first = True
        for each in reversed(A):
            res = 0
            if first:
                res = each + carry + 1
                first = False
            else:
                res = each + carry
                carry = 0
            if res > 9:
                carry = 1
                res = 0

            answer.append(res)
        if carry == 1:
            answer.append(carry)
        found_int = False
        l = []
        for each in reversed(answer):
            if each <> 0:
                found_int = True
            if found_int:
                l.append(each)


        #l = [x for x in reversed(answer)]
        return l

s = Solution()
print s.plusOne([1,2,3,5,6,7,8,9])
print s.plusOne([1,2,3,5,6,7,8,9,4,5,6,2,3,5,7])
print s.plusOne([0,0,0,1,2,3,5,6,7,8,9])
print s.plusOne([0,0,1])
print s.plusOne([0,0,9])
print s.plusOne([9])
print s.plusOne([9,9,9,9])

