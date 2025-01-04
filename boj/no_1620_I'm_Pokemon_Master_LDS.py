# 1-1. pokemon_dic[name] = idx+1를 입력한다.
# 1-2. num_dict[idx+1] = name을 입력한다.
# 2-1. 숫자가 들어오면, num_dict에서 찾는다.
# 2-2. 알파벳이 들어오면, pokemon_dict에서 찾는다.

import sys

input = sys.stdin.readline

N, M = map(int, input().split())

pokemon_dict = dict()
num_dict = dict()

for idx in range(N):
    name = input()[:-1]
    
    pokemon_dict[name] = idx+1
    num_dict[idx+1] = name

for _ in range(M):
    find_data = input()[:-1]
    
    if find_data.isdigit():
        print(num_dict[int(find_data)])
    else:
        print(pokemon_dict[find_data])