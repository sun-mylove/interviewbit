
A = [1]
B, C = 0, 0

sub_seq_sum = 0
ans = 0
index = 0
reset_index = 0

while reset_index < len(A):
    try:
        sub_seq_sum += A[index]
    except IndexError:
        index = reset_index + 1
        reset_index += 1
        try:
            sub_seq_sum = A[index]
        except IndexError:
            break

    if B <= sub_seq_sum <= C:
        ans += 1

    elif sub_seq_sum > C:
        index = reset_index
        reset_index += 1
        sub_seq_sum = 0

    index += 1

print ans
