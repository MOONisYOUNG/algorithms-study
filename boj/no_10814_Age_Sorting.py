import sys

input = sys.stdin.readline

N = int(input())

person_li = []
for idx in range(N):
    age, name = input().split()
    age = int(age)
    person_li.append((age, name, idx))
person_li.sort(key=lambda data:(data[0], data[2]))

for data in person_li:
    print(data[0], data[1])