n = int(input())

# MenOfPassion은 삼중 반복문을 배열의 원소를 더하는 알고리즘이다.
def MenOfPassion(A_li, n):
    sum_cnt = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            for k in range(1, n+1):
                sum_cnt += (A_li[i] * A_li[j] * A_li[k])
    return sum_cnt

# 삼중 반복문이므로 수행 횟수는 n ** 3이 나온다.
print(n ** 3)

# MenofPassion은 삼중 반복문을 사용하므로, 최고차항의 차수는 3이다.
print(3)