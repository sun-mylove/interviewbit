class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):

        if len(A) == 0:
            return 0

        string_list = []
        for i in xrange(len(A)):
            if A[i].isalnum():
                string_list.append(A[i])

        i, j = 0, len(string_list) - 1

        while i <= j:
            if string_list[i].lower() != string_list[j].lower():
                return 0

            i += 1
            j -= 1

        return 1

test = Solution()
print test.isPalindrome('')



