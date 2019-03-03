def calculateDistance(finishPosition, startPosition):
    if finishPosition < 0 and startPosition < 0:
        return abs(abs(finishPosition) - abs(startPosition))
    if finishPosition < 0:
        return abs(finishPosition) + startPosition
    return abs(finishPosition - startPosition)


class Solution:
    def coverPoints(self, A, B):
        i = 0
        result = 0
        while (i < len(A) - 1):
            xDiff = calculateDistance(A[i + 1], A[i])
            yDiff = calculateDistance(B[i + 1], B[i])
            if xDiff > yDiff:
                result += xDiff
            else:
                result += yDiff
            i += 1
        return result

if __name__ == '__main__':
    s =  Solution()
    print(s.coverPoints([1,3,-5,7], [4,4,7,4]))
