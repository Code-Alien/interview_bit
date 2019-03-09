class Solution:
    # @param A : list of integers
    # @return an integer
    def maxSpecialProduct(self, A):
        mod = pow(10, 9) + 7
        n = len(A)
        stack = []
        max_prod = 0

        for i, a in enumerate(A):
            while stack and a >= A[stack[-1]]:
                j = stack.pop()
                if stack and A[j] < a:
                    max_prod = max(max_prod, stack[-1] * i)
            stack.append(i)

        return max_prod % mod

if __name__ == '__main__':
    s = Solution()
    print(s.maxSpecialProduct([5, 9, 6, 8, 6, 4, 6, 9, 5, 4, 9]))
