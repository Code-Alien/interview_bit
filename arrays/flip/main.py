# @param A : string
# @return a list of integers


# My Brute Force solution:

# def flip(self, A):
#     i = 0
#     result = []
#     maxCount = A.count('1')
#     while i < len(A):
#         j = i + 1
#         tmp = list(A)
#         if tmp[i] == '0':
#             tmp[i] = '1'
#         else:
#             tmp[i] = '0'
#         if tmp.count('1') > maxCount:
#             maxCount = tmp.count('1')
#             result = [i+ 1,i + 1]
#         while j < len(A):
#
#             if tmp[j] == '0':
#                 tmp[j] = '1'
#             else:
#                 tmp[j] = '0'
#             if tmp.count('1') > maxCount :
#                 maxCount = tmp.count('1')
#                 result = [i+1, j+1]
#             j+=1
#
#         i+=1
#     return result

def kadane(A):
    maxCurrent = maxGlobal = A[0]
    i = tmp = 1
    if maxCurrent == 1:
        result = [1, 1]
    else:
        result = [None] * 2
    while i < len(A):
        if A[i] > maxCurrent + A[i]:
            tmp = i + 1
        maxCurrent = max(A[i], maxCurrent + A[i])
        if maxCurrent > maxGlobal:
            maxGlobal = maxCurrent
            result[0] = tmp
            result[1] = i + 1
        i += 1

    return result


class Solution:

    def flip(self, A):
        i = 0
        tmp = []
        i = 0
        if A.count('1') == len(A):
            return []
        while i < len(A):
            if A[i] == '1':
                tmp.append(-1)
            else:
                tmp.append(1)
            i += 1

        return kadane(tmp)


if __name__ == '__main__':
    s = Solution()
    print(s.flip("010111"))
