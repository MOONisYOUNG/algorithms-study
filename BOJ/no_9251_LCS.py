import sys

input = sys.stdin.readline

string1, string2 = input().rstrip(), input().rstrip()

h, w = len(string1), len(string2)

cache = [[0] * (w+1) for _ in range(h+1)]

for i in range(1, h+1):
    for j in range(1, w+1):
        if string1[i-1] == string2[j-1]:
            cache[i][j] = cache[i-1][j-1] + 1
        else:
            cache[i][j] = max(cache[i][j-1], cache[i-1][j])
            
print(cache[-1][-1])