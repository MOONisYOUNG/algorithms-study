import sys
input = sys.stdin.readline

n_A, n_B = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))

answer = 0
if (A - B) :
    answer = list(A - B)
    answer.sort()
    
    print(len(A-B))
    print(*answer, sep=' ')

else:
    print(answer)