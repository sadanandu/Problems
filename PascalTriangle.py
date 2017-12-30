class Solution:
    # https://www.interviewbit.com/problems/pascal-triangle/
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        triangle = []
        for x in range(A):
            if x > 0:
                triangle.append(self.generate_next_row(triangle[x-1]))
            else:
                triangle.append([1])
        return triangle

    def generate_next_row(self, row):
        ans = []
        for each in range(len(row)+1):
            try:
                c = row[each]
            except Exception:
                c = 0
            try:
                if each-1 >=0:
                    c1 = row[each-1]
                else:
                    c1 = 0
            except Exception:
                c1 = 0

            ele = c + c1
            ans.append(ele)
        return ans

s = Solution()
tri = s.generate(10)
for each in tri:
    print each


