class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A = sorted(A)
        i = 0
        found = -1
        counter = 0
        lastFoundEqual = -1
        while i < len(A) and A[i] < len(A):
            if A[i] <= len(A) - i - 1:
                j = i + 1
                while j < len(A):
                    # print(A[i],A[j], i,j)
                    if A[i] == A[j]:
                        lastFoundEqual = j
                        j += 1
                        # print(lastFoundEqual)
                        continue
                    counter = len(A) - j
                    break
                if counter == A[i]:
                    return 1
                counter = 0
            if lastFoundEqual != -1:
                i = lastFoundEqual
            lastFoundEqual = -1
            i += 1

        return found


if __name__ == '__main__':
    s = Solution()
    print(s.solve([5, 6, 2]))
