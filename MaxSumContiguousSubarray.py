class Solution:
    # @param A : tuple of integers
    # @return an integer
    def __init__(self):
        self.sum_of_subarray_from = {}

    def maxSubArray(self, A):
        #self.sum_of_subarray_from.update([(index, each) for index, each in enumerate(A)])
        self.sum_of_subarray_from = {}
        for index, each in enumerate(A):
            self.sum_of_subarray_from[index] = self.find_sum_of_subarray_starting_from(index, A)
            '''if index+1 in self.sum_of_subarray_from:
                if each + self.sum_of_subarray_from[index + 1] > each:
                    self.sum_of_subarray_from[index] += self.find_sum_of_subarray_starting_from(index +1) # self.sum_of_subarray_from[index + 1]'''
        return max(self.sum_of_subarray_from.values())
        #return self.sum_of_subarray_from

    def find_sum_of_subarray_starting_from(self, index, A):
        if index > len(A) -1:
            return 0
        if index in self.sum_of_subarray_from:
            return self.sum_of_subarray_from[index]
        else:
            s = self.find_sum_of_subarray_starting_from(index + 1, A)
            if s > 0:
            #if A[index] + s >= A[index]:
                self.sum_of_subarray_from[index] = A[index] + s
                return self.sum_of_subarray_from[index]
            else:
                return A[index]
s = Solution()
print s.maxSubArray([3,2,-1,4,5,1])
print s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print s.maxSubArray([1,0,0,0])
'''
1. Store sum of alements starting from index and reuse it
2. Add next subarray to current only if it increases the value
   else move over to the next element in dict and start from there
   what is the end condition
3. find max from sum_of_subarray dict

'''