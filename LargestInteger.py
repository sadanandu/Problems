class Solution:
    # https://www.interviewbit.com/problems/largest-number/
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        num = []
        sA = [str(each) for each in A]
        index = 0
        tries = 0
        while sA:
            largest = -1
            if len(sA) <> 1:
                all_same = True
            else:
                all_same = False
            '''print 'cehcking for ', sA
            print 'index', index
            print 'largest is', largest'''
            for each in sA:
                try:
                    #if largest <> -1:
                    #    if len(each) > index and int(each[index]) <> int(str(largest)[index]):
                    #        all_same = False

                    #if int(each[:index+1]) > largest:
                        #largest = int(each)
                    #if current digit of each > current of largest then largest = each
                    if largest == -1:
                        largest = int(each)
                        continue

                    #Set all_same tag
                    ind_for_each = self.get_valid_index_for(each, index)
                    ind_for_largest = self.get_valid_index_for(largest, index)
                    if int(each[ind_for_each]) <> int(str(largest)[ind_for_largest]):
                        all_same = False
                    '''if len(each) > index and len(largest) > index: #can take the current index
                        if int(each[index]) <> int(str(largest)[index]):
                            all_same = False
                    else:
                        if int(each[-1]) <> int(str(largest)[-1]):
                            all_same = False'''
                    if int(each[ind_for_each]) > int(str(largest)[ind_for_largest]):
                        largest = int(each)

                    # change largest
                    '''if len(each) > index and len(largest) > index: #can take the current index
                        if int(each[index]) > int(str(largest)[index]):
                            largest = int(each)
                    else:
                        if int(each[-1]) > int(str(largest)[-1]):
                            largest = int(each)'''


                    '''if len(each) > index and int(each[index]) > largest:
                        largest = int(each)
                    #print 'checking', str(int(each[:index+1])), ' >', str(largest)
                    #print 'len(each) <= index', len(each) <= index
                    #print 'int(each[:index+1]) > largest', int(each[:index+1]) > largest
                    if len(each) <= index and int(each[:index+1]) > largest:
                        largest = int(each)'''
                except Exception, e:
                    pass
            #print 'largest', largest
            if all_same:
                #print 'allsame'
                index += 1
                '''n = min(sA)
                num.append(str(n))
                sA.remove(str(n))'''
            else:
                num.append(str(largest))
                index = 0
                sA.remove(str(largest))
        return ''.join(num)

    def get_valid_index_for(self, num , index):
        while True:
            try:
                str(num)[index]
                break
            except Exception, e:
                index -= 1
        return index

s = Solution()
'''print s.largestNumber([1,2, 3])
print '*'*8
print s.largestNumber([9,8,7])
print '*'*8
print s.largestNumber([1])
print '*'*8'''
#print s.largestNumber([30,31, 320])
#print s.largestNumber([30, 320,31])

print '*'*8
print s.largestNumber([1,2,1])

#3, 31, 320
#332031
