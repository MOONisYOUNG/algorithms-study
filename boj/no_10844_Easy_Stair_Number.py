N = int(input())

d = [[0]*10 for _ in range(N+1)]
for i in range(1, 10):
    d[1][i] = 1
    
mod = 10**9

def solution():
    for i in range(2, N+1):
        for j in range(10):
            if j == 0:
                d[i][j] = d[i-1][1]
            
            elif j == 9:
                d[i][j] = d[i-1][8]
                
            else:
                d[i][j] = d[i-1][j-1] + d[i-1][j+1]
                
    return sum(d[N]) % mod
    

print(solution())