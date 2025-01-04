# 1. B진법 딕셔너리를 정의한다. 
# 2. 뒤집은 N(N[::-1])을 for 반복문을 써서 10진법으로 변환시킨다. 
    # 2-1. N[k] 단위로 접근해서 계산한다.

N, B = input().split()
B = int(B)

B_dict = dict()

for k in range(0, 10):
    B_dict[str(k)] = k
    
for k in range(ord('A'), ord('Z')+1):
    B_dict[chr(k)] = k - 55

answer = 0
pos = 0
for n in N[::-1]:
    answer += (B_dict[n] * (B ** pos))
    pos += 1
    
print(answer)