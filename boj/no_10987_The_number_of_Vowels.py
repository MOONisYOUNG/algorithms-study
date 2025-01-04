import sys
input = sys.stdin.readline

word = input()[:-1]
answer = len(tuple(filter(lambda x : x in {'a', 'e', 'i', 'o', 'u'}, word)))
        
print(answer)