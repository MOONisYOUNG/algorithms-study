# 0. 막대의 크기를 늘릴 수는 없고, 줄이는 것만 가능하다.
# 1. 막대 길이를 리스트(stick_li)에 넣은 후, 정렬을 실시한다.
# 2. stick_li[0] + stick_li[1] > stick_li[2]를 만족하는지 확인한다.
    # 2-1. 위 조건을 만족하지 않는다면, stick_li[2] 값을 줄여준다.
    # 2-2. stick_li[2] = stick_li[0] + stick_li[1] - 1로 길이를 조절한다.
# 3. sum(stick_li)를 해서 둘레 길이를 구한다.

stick_li = list(map(int, input().split()))
stick_li.sort()

if not (stick_li[0] + stick_li[1] > stick_li[2]):
    stick_li[2] = stick_li[0] + stick_li[1] - 1
    
answer = sum(stick_li)
print(answer)