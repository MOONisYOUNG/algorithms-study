import sys
input = sys.stdin.readline

while True:
    n = int(input())
    
    if n == 0:
        break
    
    word_li = []
    for _ in range(n):
        word = input().rstrip()
        word_li.append((word, word.lower()))
        
    word_li = sorted(word_li, key = lambda x : x[1])
    
    print(word_li[0][0])