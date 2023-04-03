import sys

A, K = map(int, sys.stdin.readline().split())
A_li = list(map(int, sys.stdin.readline().split()))

def merge_sort(A_li):
  global move_element_li
  n = len(A_li)
  
  if n == 1:
    return A_li
  
  mid = (n+1) // 2
  group_1 = merge_sort(A_li[:mid])
  group_2 = merge_sort(A_li[mid:])

  i, j = 0, 0
  result = []
  while i < len(group_1) and j < len(group_2):
    if group_1[i] < group_2[j]:
      result.append(group_1[i])
      move_element_li.append(group_1[i])
      i += 1
    else:
      result.append(group_2[j])
      move_element_li.append(group_2[j])
      j += 1

  while i < len(group_1):
    result.append(group_1[i])
    move_element_li.append(group_1[i])
    i += 1
  while j < len(group_2):
    result.append(group_2[j])
    move_element_li.append(group_2[j])
    j += 1
    
  return result


move_element_li = []
merge_sort(A_li)

if len(move_element_li) < K:
  print(-1)
else:
  print(move_element_li[K-1])