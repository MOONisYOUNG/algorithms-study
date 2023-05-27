# 1. num_li에 set을 취한 뒤, 다시 list로 바꿔준 후에 not_duple_num_li에 저장한다.
# 2. not_duple_num_li 정렬 연산한다.
# 3. not_duple_num_li의 원소에 index 정보를 함께 붙여서 not_duple_num_dict에 저장한다. 
# 4. num_li에 not_duple_num_dict를 대조해서 인덱스 값을 출력한다.

N = int(input())
num_li = list(map(int, input().split()))

not_duple_num_li = sorted(list(set(num_li)))
not_duple_num_dict = {val:idx for idx, val in enumerate(not_duple_num_li)}

for data in num_li:
    print(not_duple_num_dict[data], end=' ')