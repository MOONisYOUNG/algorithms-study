n = int(input())

# MenOfPassion은 삼중 반복문을 배열의 원소를 더하는 알고리즘이다.
def MenOfPassion(A_li, n):
    sum_cnt = 0
    for i in range(1, n-1):
        for j in range(i+1, n):
            for k in range(j+1, n+1):
                sum_cnt += (A_li[i] * A_li[j] * A_li[k])
    return sum_cnt

# 등차수열을 이용해서 수행 횟수를 구할 수 있다.
# k의 범위를 n-2부터 1까지라고 한정한 후, (k+1) * k // 2 값을 각각 구해서 더하면 된다.
cnt = 0
for k in range(n-2, 0, -1):
    cnt += ((k+1) * k // 2)
print(cnt)

# MenofPassion은 삼중 반복문을 사용하므로, 최고차항의 차수는 3이다.
print(3)