n = int(input())

# MenOfPassion은 이중 반복문을 통해 배열의 모든 원소를 더하는 알고리즘이다.
def MenOfPassion(A_li, n):
    sum_cnt = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            sum_cnt += (A_li[i] * A_li[j])
    return sum_cnt

# 따라서 MenofPssion의 수행 횟수는 n**2이다. 이중 반복문을 사용하기 때문이다.
print(n**2)

# MenofPassion의 수행 횟수는 n**2이므로, 최고차항의 차수는 2이다.
print(2)