class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        A_set = set(A)
        A_dict = {}
        A_key_set = set([])

        i = 0
        while True:
            # elem = A[i]
            if A[i] in A_key_set:
                i += 1
                if i == len(A):
                    break
                continue

            low = A[i] - 1
            high = A[i] + 1

            count = 0
            while self.is_available(A_set, low):
                A_set.remove(low)
                # A.remove(low)
                count += 1
                low -= 1

            while self.is_available(A_set, high):
                A_set.remove(high)
                # A.remove(high)
                count += 1
                high += 1

            print A[i], count
            A_dict[A[i]] = count
            A_key_set.add(A[i])

            i += 1

            if i == len(A):
                break

        print A_dict

        if len(A_dict) == 0:
            print 1
            # return 1
        else:
            print max(A_dict.values()) + 1
            # return max(A_dict.values()) + 1

    def is_available(self, A_set, val):
        if val in A_set:
            return True
        else:
            return False

sol = Solution()
sol.longestConsecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5])



