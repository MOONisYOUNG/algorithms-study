import sys

input = sys.stdin.readline

N, M = map(int, input().split())

board = []
for _ in range(N):
    board.append(input().rstrip())
    
result = []
for i in range(N-7):
    for j in range(M-7):
        case1 = 0
        case2 = 0
        
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b) % 2 == 0:
                    if board[a][b] != 'B':
                        case1 += 1
                    elif board[a][b] != 'W':
                        case2 += 1
                        
                else:
                    if board[a][b] != 'W':
                        case1 += 1
                    elif board[a][b] != 'B':
                        case2 += 1
                        
        result.append(case1)
        result.append(case2)
        
print(min(result))