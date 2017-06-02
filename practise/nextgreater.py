A = [ 34, 35, 27, 42, 5, 28, 39, 20, 28 ]
ans = []
for i in xrange(len(A)):
    next_g = -1
    iter_ind = i + 1

    while iter_ind < len(A):
        if A[iter_ind] > A[i]:
            next_g = A[iter_ind]
            break

        iter_ind += 1
    ans.append(next_g)

print ans