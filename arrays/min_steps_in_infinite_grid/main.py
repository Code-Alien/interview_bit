def calculateDistance(x1, x0):
    if x1 < 0 and x0 < 0:
        return abs(abs(x1) - abs(x0))
    if x1 < 0:
        return abs(x1) + x0
    return abs(x1 - x0)


class Solution:
    def coverPoints(self, A, B):
        i = 0
        j = 0
        while (i < len(A) - 1):
            xDiff = calculateDistance(A[i + 1], A[i])
            yDiff = calculateDistance(B[i + 1], B[i])
            if xDiff > yDiff:
                j += xDiff
            else:
                j += yDiff
            i += 1
        return j
