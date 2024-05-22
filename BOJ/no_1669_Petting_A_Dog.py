import sys
input = sys.stdin.readline

x, y = map(int, input().split())
sub = y - x

# 둘 사이에 키 차이가 없는 경우
if sub == 0:
    answer = 0

# 둘 사이에 키 차이가 존재하는 경우
else:
    # 원숭이가 가질 수 있는 가장 큰 키(=최대 제곱수) 구하기
    square_num = 1
    while square_num**2 <= sub:
        square_num += 1
    square_num -= 1
    
    # 원숭이가 가질 수 있는 최소 일자 값
    answer = 2*square_num - 1
    
    # 추후에 원숭이가 구해야 하는 나머지 키의 합산 값
    sub -= (square_num ** 2)
    
    # 나머지 키 합산 값을 기준으로 추가 일자 구하기
    while sub > 0:
        for i in range(square_num, 0, -1):
            if i <= sub:
                answer += 1
                sub -= i
                break
            else:
                continue
        
print(answer)