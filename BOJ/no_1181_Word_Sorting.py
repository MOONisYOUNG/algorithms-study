import sys

input = sys.stdin.readline

N = int(input())

word_set = set()

for _ in range(N):
    word_set.add(input().rstrip())
    
word_li = sorted(list(word_set))
word_li.sort(key=lambda data : len(data))

 
for idx in range(len(word_li)):
    print(word_li[idx])
