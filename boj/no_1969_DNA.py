import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dna_li = [input()[:-1] for _ in range(n)]

hamming_distance = 0
answer_dna = ''

for i in range(m):
    cnt_li = [['A', 0], ['T', 0], ['C', 0], ['G', 0]]
    for j in range(n):
        target = dna_li[j][i]
        if target == 'A':
            cnt_li[0][1] += 1
            
        elif target == 'T':
            cnt_li[1][1] += 1
            
        elif target == 'C':
            cnt_li[2][1] += 1
            
        else:
            cnt_li[3][1] += 1
    
    # 영어는 오름차순, 숫자는 내림차순으로 정렬
    max_val = min(cnt_li, key=lambda x:(-x[1], x[0]))
    answer_dna += max_val[0]
    # Hamming Distance의 합을 구하는 것이므로 행/열 기준 상관 없이 결과는 동일
    hamming_distance += (n - max_val[1])
    
print(answer_dna, hamming_distance, sep='\n')