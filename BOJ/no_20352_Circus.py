from math import pi

area = int(input())
radius = (area / pi) ** 0.5
answer = 2 * pi * radius

print(round(answer, 10))