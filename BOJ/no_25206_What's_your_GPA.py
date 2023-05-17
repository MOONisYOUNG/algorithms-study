import sys

input = sys.stdin.readline

grade_dict = {"A+":4.5, "A0":4.0, "B+":3.5, "B0":3.0, "C+":2.5, "C0":2.0, 
              "D+":1.5, "D0":1.0, "F":0.0}

total_credit = 0
numerator = 0

for _ in range(20):
        _ , credit, grade = input().split()
        credit = float(credit)
        
        if grade == "P":
            continue

        total_credit += credit
        numerator += credit * grade_dict[grade]
        
answer = numerator / total_credit
print(round(answer, 6))