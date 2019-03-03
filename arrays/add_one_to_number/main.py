def removeLeadingZero(A):
    i = 0
    count = 0
    # left last 0
    while i < len(A) - 1:
        if A[i] == 0:
            count += 1
        else:
            break
        i += 1
    return A[count:]


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        A = removeLeadingZero(A)
        shouldAddOne = False
        i = len(A) - 1
        while i >= 0:
            if A[i] == 9:
                A[i] = 0
                shouldAddOne = True
            else:
                A[i] = A[i] + 1
                shouldAddOne = False
            if not shouldAddOne:
                break
            i -= 1
        if shouldAddOne:
            B = [1]
            A = B + A
        return A


if __name__ == '__main__':
    s = Solution()
    print(s.plusOne([0, 0]))
