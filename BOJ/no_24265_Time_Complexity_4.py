n = int(input())

# MenOfPassion은 이중 반복문을 배열의 원소를 더하는 알고리즘이다.
def MenOfPassion(A_li, n):
    sum_cnt = 0
    for i in range(1, n):
        for j in range(i+1, n+1):
            sum_cnt += (A_li[i] * A_li[j])
    return sum_cnt

# 더하는 횟수는 등차수열 공식을 통해 계산할 수 있다.
# 정리하면 n * (n-1) / 2 가 나온다.
print(int(n * (n-1) / 2))

# MenofPassion은 이중반복문을 사용하므로, 최고차항의 차수는 2이다.
print(2)