import sys
input = sys.stdin.readline

yeondoo = input()[:-1]
n = int(input())
team_names = [input()[:-1] for _ in range(n)]

# collections.Counter 사용하는 것보다 빌트인 count 함수 쓰는 것이 더 효율적
winning_rates = []
for team in team_names:
    l = yeondoo.count('L') + team.count('L')
    o = yeondoo.count('O') + team.count('O')
    v = yeondoo.count('V') + team.count('V')
    e = yeondoo.count('E') + team.count('E')
    
    val = ((l+o) * (l+v) * (l+e) * (o+v) * (o+e) * (v+e)) % 100
    winning_rates.append([val, team])

# 승률 내림차순, 팀 이름 오름차순 정렬
winning_rates.sort(key=lambda x:(-x[0], x[1]))
answer = winning_rates[0][1]
print(answer)