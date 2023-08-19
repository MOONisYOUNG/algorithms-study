import sys
input = sys.stdin.readline

name_li = [input().rstrip() for _ in range(5)]

fbi_idx_li = []
for idx, name in enumerate(name_li):
    if 'FBI' in name:
      fbi_idx_li.append(idx+1)
      
if fbi_idx_li:
    print(*fbi_idx_li, sep=' ')
else:
    print('HE GOT AWAY!')