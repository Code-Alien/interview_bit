class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A = sorted(A)
        i = 0
        while i < len(A) - 1:
            key = A[i]
            A[i] = A[i+1]
            A[i + 1] = key
            i+=2

        return A


if __name__ == '__main__':
    s = Solution()
    print(s.wave([1,2,3,4]))