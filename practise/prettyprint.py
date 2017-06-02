
A = 4

matrix_size = 2 * (A - 1) + 1

for i in xrange(matrix_size):
    for j in xrange(matrix_size):
        if i > A - 1:
            i = matrix_size - 1 - i
        if j > A- 1:
            j = matrix_size - 1 - j

        if i <= j <= matrix_size - 1 - i:
            print A - i,

        elif j <= i <= matrix_size - 1 - j:
            print A - j,

    print
