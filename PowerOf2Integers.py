class Solution:
    # https://www.interviewbit.com/problems/power-of-two-integers/
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        #A^P A>0 & P >1
        factors = self.find_factors(A)
        d = {}
        if len(factors) == 1:
            return 0
        for each in factors:
            if each not in d:
                d[each] = 1
            else:
                d[each] += 1

        if len(set(d.values())) > 1:

            factors_of_factor_powers = [self.find_factors(each) for each in d.values()]
            #print d.values()
            #print factors_of_factor_powers
            common = set(factors_of_factor_powers[0])
            for each in factors_of_factor_powers[1:]:
                common = common& set(each)
            #print common
            if common:
                return 1
            else:
                return 0
            '''factor_powers = sorted(d.values())
            s = factor_powers[0]
            for each in factor_powers[1:]:
                if not each%s == 0:
                    return 0
            return 1'''
        else:
            if list(set(d.values())) == [1]:
                return 0
            return 1


    def find_factors(self, A):
        factors = []
        num = A
        while num <> 1:
            #print 'num', num
            for i in xrange(2, A+1):
                #print 'for ', i
                if num%i == 0:
                    #print 'got factor'
                    factors.append(i)
                    num = num/i
                    break
        return factors

s = Solution()
print s.isPower(50074)



