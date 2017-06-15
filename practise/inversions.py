

class Solution:
    # @param A : list of integers
    # @return an integer
    def merge_sort(self, alist, inversions):

        alist_length = len(alist)

        # check if the list length is less than or equal to 1
        # If yes, return that list (single element); lest call the same function
        # until the list is broken down to one element length (base case)

        if alist_length <= 1:
            return alist, inversions

        else:
            split = alist_length / 2

            left = alist[:split]
            right = alist[split:]

            if len(left) > 1:
                left, inversions = self.merge_sort(left, inversions)

            if len(right) > 1:
                right, inversions = self.merge_sort(right, inversions)

            # merge function is called with arguments, left and right halves produced
            # in that specific merge_sort function, as part of each recursive call to merge_sort

            # printing arguments to each merge call
            # print "calling merge with arguments", left, ";", right

            return self.merge(left, right, inversions)

    def merge(self, l, r, inversions):

        l_length = len(l)
        r_length = len(r)
        i, j = 0, 0

        left_elements_added = 0

        slist = []

        # actual sort operation happens in "merge" routine
        # as part of below while and if-else blocks

        while i < l_length and j < r_length:

            if l[i] <= r[j]:
                slist.append(l[i])
                i += 1

                # this variable keeps a counter on number of elements
                # in left half added to sorted list
                left_elements_added += 1

            else:
                slist.append(r[j])
                j += 1

                # inversions is sum of number of elements in left half NOT
                # added to sorted list , every time an element from
                # right half is written to sorted list

                inversions += l_length - left_elements_added

        if i < l_length:
            while i < l_length:
                slist.append(l[i])
                i += 1
        else:
            while j < r_length:
                slist.append(r[j])
                j += 1

        # printing output of merge call
        # print "Output from merge:", slist

        return slist, inversions

    def countInversions(self, A):
        inversions = 0
        sorted_A, inversions = self.merge_sort(A, inversions)
        return inversions


test = Solution()

inp = [2, 4, 1, 3, 5]

print test.countInversions(inp)
