# 0. 반복문을 5번 사용해서 데이터를 입력받는다.
    # 0-1. 데이터 길이가 15보다 작으면, 길이 15가 될 때까지 -1로 채워 넣는다.
# 1. 이중 반복문을 사용해서 데이터를 세로로 읽어서 string 변수에 저장한다.
    # 1-1. 만약 원소값이 -1이 아니라면, string 변수에 저장한다.
    
import sys

input = sys.stdin.readline

data_li = []
for _ in range(5):
    data = list(input())[:-1]
    data_len = len(data)
    if data_len < 15:
        data += [-1] * (15 - data_len)
    data_li.append(data)
    
answer = ''
for idx_1 in range(15):
    string = ''
    for idx_2 in range(5):
        data = data_li[idx_2][idx_1]
        if data != -1:
            string += data
    answer += string
    
print(answer)