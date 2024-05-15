import sys
from collections import Counter
input = sys.stdin.readline

yeondoo_name = input()[:-1]
yeondoo_counter = Counter(yeondoo_name)
n = int(input())
team_names = [input()[:-1] for _ in range(n)]

winning_rates = []
for team in team_names:
    team_counter = Counter(team)
    
    l = yeondoo_counter['L'] + team_counter['L']
    o = yeondoo_counter['O'] + team_counter['O']
    v = yeondoo_counter['V'] + team_counter['V']
    e = yeondoo_counter['E'] + team_counter['E']
    
    val = ((l+o) * (l+v) * (l+e) * (o+v) * (o+e) * (v+e)) % 100
    winning_rates.append([val, team])

# 승률 내림차순, 팀 이름 오름차순 정렬
winning_rates.sort(key=lambda x:(-x[0], x[1]))
answer = winning_rates[0][1]
print(answer)