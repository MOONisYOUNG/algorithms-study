import sys
input = sys.stdin.readline

n, m = map(int, input().split())

def solution(n: int, m: int) -> int:
    row_tf_li = [False for _ in range(n)]
    col_tf_li = [False for _ in range(m)]
    
    for i in range(n):
        row = input()[:-1]
        
        for j in range(m):
            if row[j] == 'X':
                row_tf_li[i] = True
                col_tf_li[j] = True
    
    col_f_cnt = col_tf_li.count(False)
    row_f_cnt = row_tf_li.count(False)
    
    answer = max(col_f_cnt, row_f_cnt)
    
    return answer
    
print(solution(n, m))