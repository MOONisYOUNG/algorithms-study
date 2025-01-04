# 0. 케이스 숫자들을 num_li에 저장한다.
# 1. 숫자 list의 최대값을 구해서 저장한다. max_num = max(num_li)
# 2. 2 ~ max_num까지 소수를 구해서 prime_num_li에 저장한다. 
  # 2-1. 이때, 에라토스테네스의 체를 사용해서 구한다. 
  # 2-2. 에라토스테네스의 체는 소거법 형태로 이뤄진다.
  # 2-3. 소수는 True, 소수가 아닌 건 False로 저장한다.
# 3. prime_num_li 속 두 값이 True이면서, 인덱스 합이 num인 경우만 개수를 센다.

import sys
input = sys.stdin.readline

def prime_num_sieve(num):
  array = [True for _ in range(num+1)]
  array[0], array[1] = False, False

  for i in range(2, int(num**0.5)+1):
    if array[i]:
      j = 2

    while i * j <= num:
      array[i * j] = False
      j += 1
      
  return array


T = int(input())

num_li = [int(input()) for _ in range(T)]
max_num = max(num_li)

prime_num_li = prime_num_sieve(max_num)

for num in num_li:
  answer = 0

  for k in range(2, num//2 + 1):
    if prime_num_li[k] and prime_num_li[num-k]:
      answer += 1

  print(answer)