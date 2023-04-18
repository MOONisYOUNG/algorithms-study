import sys

input = sys.stdin.readline

N, M, B = map(int, input().split())

land_data = []
for _ in range(N):
    land_data.append(list(map(int, input().split())))
    
time = int(1e9)
ground_height = 0

for i in range(257):
    use_block = 0
    take_block = 0
    for x in range(N):
        for y in range(M):
            if land_data[x][y] > i:
                take_block += land_data[x][y] - i
            else:
                use_block += i - land_data[x][y]
                
    if use_block > take_block + B:
        continue
    
    temp = take_block * 2 + use_block
    
    if temp <= time:
        time = temp
        ground_height = i
        
print(time, ground_height)