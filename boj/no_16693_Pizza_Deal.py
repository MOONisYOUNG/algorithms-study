from math import pi

A1, P1 = map(int, input().split())
R1, P2 = map(int, input().split())

A2 = (R1**2) * pi

if A1/P1 > A2/P2:
    print("Slice of pizza")
else:
    print("Whole pizza")