input_li = list(map(int, input().split()))
chess_li = [1, 1, 2, 2, 2, 8]

answer_li = [(chess_li[i] - input_li[i]) for i in range(len(input_li))]

for data in answer_li:
    print(data, end=' ')