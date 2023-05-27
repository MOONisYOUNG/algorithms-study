# 0. num_li = list(map(int, list(input())))을 사용해서 입력받는다.
# 1. num_li.sort(reverse=True)
# 2. print(*num_li, sep='')을 사용해서 답을 출력한다.

num_li = list(map(int, list(input())))
num_li.sort(reverse=True)

print(*num_li, sep='')