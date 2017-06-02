# from collections import dequeu



class Solution:
    # @param A : list of integers
    # @return a list of integers

    def plusOne(self, A):

        # most_significant_digit_found = False

        # print A

        if A[0] == 0 and len(A) > 1:
            inp = list(reversed(A))
            while True:
                if inp[-1] == 0:
                    del inp[-1]
                else:
                    break

            A = list(reversed(inp))

        if len(A) == 1:
            last_digit = A.pop()

            if last_digit == 9:
                A = [1, 0]
            else:
                A.append(last_digit + 1)

            return A

        # print A
        # return self.answer(A)

        ans = []
        while len(A) != 0:
            last_digit = A.pop()

            if last_digit == 9:
                ans.append(0)

            else:
                A.append(last_digit + 1)
                break

        if len(A) == 0:
            return [1] + list(reversed(ans))
        else:
            return A + list(reversed(ans))


test = Solution()
print test.plusOne([k for k in xrange(10)])
