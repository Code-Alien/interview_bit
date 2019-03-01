class Solution:

    def fizzBuzz(self, A):
        i = 1
        result = []
        while (i <= A):
            s = ""
            if i % 3 == 0:
                s += "Fizz"
            if i % 5 == 0:
                s += "Buzz"
            if len(s) > 0 :
                result.append(s)
            else:
                result.append(i)
            i += 1
        return result


if __name__ == '__main__':
    s = Solution()
    print(str(s.fizzBuzz(15))[1:-1])
