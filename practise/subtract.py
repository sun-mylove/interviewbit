# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def subtract(self, A):
        A_initial = A
        inp_list = []
        while True:
            if A.next is None:
                inp_list.append(A.val)
                break
            inp_list.append(A.val)
            A = A.next

        inp_len = len(inp_list)
        updated_list = []
        i, j = 0, inp_len - 1
        while True:
            if i == inp_len / 2 or j == inp_len / 2:
                updated_list.append(inp_list[j] - inp_list[i])
                break
            updated_list.append(inp_list[j] - inp_list[i])
            i += 1
            j -= 1

        A = A_initial
        for i in xrange(len(updated_list)):
            A.val = updated_list[i]
            A = A.next
        return A_initial
