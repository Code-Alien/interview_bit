# LeftSpecialValue: For an index i, it is defined as the index j such that A[j]>A[i] (i>j).
# If multiple A[j]’s are present in multiple positions, the LeftSpecialValue is the maximum value of j.
def findLeftSpecialValue(A, i):
    j = i - 1
    leftSpecial = 0
    while j >= 0:

        if A[j] > A[i]:
            return j

        j -= 1
    return leftSpecial


# RightSpecialValue: For an index i, it is defined as the index j such that A[j]>A[i] (j>i).
# If multiple A[j]s are present in multiple positions, the RightSpecialValue is the minimum value of j.

def findRightSpecialValue(A, i):
    j = i + 1
    rightSpecial = 0
    while j < len(A):
        if A[j] > A[i]:
            return j
        j += 1
    return rightSpecial


class Solution:
    # @param A : list of integers
    # @return an integer
    def maxSpecialProduct(self, A):
        if len(A) < 2:
            return 0
        i = 1
        result = []
        while i < len(A):
            result.append(findLeftSpecialValue(A, i) * findRightSpecialValue(A, i))
            i += 1
        return max(result) % 1000000007


if __name__ == '__main__':
    s = Solution()
    print(s.maxSpecialProduct([ 5, 9, 6, 8, 6, 4, 6, 9, 5, 4, 9]))
