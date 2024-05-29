import sys
input = sys.stdin.readline

first, second, third = [input()[:-1] for _ in range(3)]

resistor = {'black':'0', 'brown':'1', 
            'red':'2', 'orange':'3',
            'yellow':'4', 'green':'5', 
            'blue':'6', 'violet':'7',
            'grey':'8', 'white':'9'}
    
answer = int((resistor[first]+resistor[second])) * (10**int(resistor[third]))
print(answer)