import sys
input = sys.stdin.readline

n, m = map(int, input().split())
array = [list(map(int, list(input()[:-1]))) for _ in range(n)]

answer = -1

# Brute-Force 방식을 사용해서 하나씩 검증
for i in range(n):
    for j in range(m):
        for di in range(-n, n):
            for dj in range(-m, m):
                
                if (di == 0) and (dj == 0):
                    continue
                
                now_i = i; now_j = j; now_val = 0;
                
                while (0 <= now_i < n) and (0 <= now_j < m):
                    now_val *= 10
                    now_val += array[now_i][now_j]
                    
                    sqrt_check = int(now_val ** 0.5)
                    if sqrt_check**2 == now_val:
                        answer = max(answer, now_val)
                        
                    now_i += di; now_j += dj;
                    
print(answer)