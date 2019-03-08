def findIndexOfFirstPositiveNumber(A):
    i = 0
    while i < len(A):
        if A[i] >= 0:
            return i
        i += 1

    return -1


class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        try:
            iterator = iter(A)
        except TypeError:
            if A >= 0:
                return A
            else:
                return []

        firstIndex = findIndexOfFirstPositiveNumber(A)
        if firstIndex == -1:
            return []

        i = firstIndex + 1
        maxSum = currentSum = A[firstIndex]
        result = []

        while i < len(A):
            if A[i] >= 0:
                if firstIndex == -1:
                    firstIndex = i
                currentSum += A[i]
            if A[i] < 0 or i == len(A) - 1:
                if currentSum >= maxSum:
                    if currentSum > maxSum:
                        result = []

                    maxSum = currentSum

                    if A[i] < 0:
                        result.append(A[firstIndex:i])
                    else:
                        result.append(A[firstIndex:])

                firstIndex = -1
                currentSum = 0

            i += 1

        if len(result) == 0:
            return [A[firstIndex]]

        maxSegmentLength = len(result[0])
        segId = 0
        i = 1
        while i < len(result):
            if len(result[i]) > maxSegmentLength:
                maxSegmentLength = len(result[i])
                segId = i

            i += 1

        return result[segId]

if __name__ == '__main__':
    s = Solution()
    print(s.maxset(
        [24831, 53057, 19790, -10679, 77006, -36098, 75319, -45223, -56760, -86126, -29506, 76770, 29094, 87844, 40534,
         -15394, 18738, 59590, -45159, -64947, 7217, -55539, 42385, -94885, 82420, -31968, -99915, 63534, -96011, 24152,
         77295]))