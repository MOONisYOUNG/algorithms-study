import sys
N = int(sys.stdin.readline().rstrip())

def hanoi_tower(N, start, end):
    if N == 1:
        print(start, end)
        return
    
    hanoi_tower(N-1, start, 6-start-end)
    print(start, end)
    hanoi_tower(N-1, 6-start-end, end)
    
    
print(2**N - 1)
hanoi_tower(N, 1, 3)