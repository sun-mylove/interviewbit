class Solution:
    # @param A : string
    # @return an integer

    def isPalindrome(self, A):

        if len(A) == 0:
            return 0

        i, j = 0, len(A) - 1

        while i <= j:
            if A[i] != A[j]:
                return False
            
            i += 1
            j -= 1

        return True

    def solve(self, A):

        length_of_A = len(A)
        length_of_palindromes = [0]

        for i in xrange(len(A) + 1):
            if self.isPalindrome(A[0:i]):
                length_of_palindromes.append(i)

        return length_of_A - max(length_of_palindromes)

test = Solution()
print test.solve('')
