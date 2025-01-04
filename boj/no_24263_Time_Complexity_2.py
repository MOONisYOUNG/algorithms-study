n = int(input())

# MenOfPassion은 배열의 모든 원소를 더하는 알고리즘이다.
def MenOfPassion(A_li, n):
    sum_cnt = 0
    for i in range(1, n+1):
        sum_cnt += A_li[i]
    return sum_cnt

# 따라서 MenofPssion의 수행 횟수는 n이다. 배열의 개수에 영향을 받기 때문이다.
print(n)

# MenofPassion의 수행 횟수는 n이므로, 최고차항의 차수는 1이다.
print(1)