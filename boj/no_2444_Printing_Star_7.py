N = int(input())

for k in range(1, N):
    print(' '*(N-k) + '*'*(2*k-1))
for k in range(N, 0, -1):
    print(' '*(N-k) + '*'*(2*k-1))