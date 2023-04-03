import sys

T = int(sys.stdin.readline())

def recursion(S, left, right):
  global recursion_cnt
  if left >= right:
    return 1
  elif S[left] != S[right]:
    return 0
  else:
    recursion_cnt += 1
    return recursion(S, left+1, right-1)

def isPalindrome(S):
  return recursion(S, 0 , len(S)-1)


for _ in range(T):
  S = sys.stdin.readline()[:-1]

  # 기본적으로 1번은 무조건 불러오기 때문에 1로 초기화
  recursion_cnt = 1 
  answer_1st = isPalindrome(S)
  answer_2nd = recursion_cnt
  
  print(answer_1st, answer_2nd)