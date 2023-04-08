import sys

input = sys.stdin.readline

M = int(input())

set_to_solve = set()
for _ in range(M):
    command = input().split()
    
    if command[0] == "add":
        set_to_solve.add(int(command[1]))
        
    elif command[0] == "remove":
        set_to_solve.discard(int(command[1]))
        
    elif command[0] == "check":
        if int(command[1]) in set_to_solve:
            print(1)
        else:
            print(0)
            
    elif command[0] == "toggle":
        if int(command[1]) in set_to_solve:
            set_to_solve.discard(int(command[1]))
        else:
            set_to_solve.add(int(command[1]))
            
    elif command[0] == "all":
        set_to_solve = {num for num in range(1, 21)}
        
    elif command[0] == "empty":
        set_to_solve = set()