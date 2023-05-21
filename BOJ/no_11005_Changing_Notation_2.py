# 1. N을 더 나눌 수 없을 때까지, N을 B로 나눈 나머지를 빈 리스트에 집어넣는다.
# 2. 리스트에 있는 요소들을 하나씩 B진법 문자로 치환시켜 준다.
# 3. 리스트 속 내용물들을 거꾸로 결합시키면, 답을 구할 수 있다.

N, B = map(int, input().split())

change_B = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

B_li = []
while N > 0:
    B_li.append(change_B[N % B])
    N //= B
    
answer = ''.join(B_li[::-1])
print(answer)