import sys
input = sys.stdin.readline

def solution(n: int, m: int) -> int:
    truth_knowers_input = list(map(int, input().split()))
    truth_knowers = set(truth_knowers_input[1:])

    parent = list(range(n + 1))

    def find(x: int) -> int:
        if parent[x] == x:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def union(x: int, y: int):
        root_x = find(x)
        root_y = find(y)
        
        if root_x != root_y:
            if root_x in truth_knowers:
                parent[root_y] = root_x
            
            elif root_y in truth_knowers:
                parent[root_x] = root_y
            
            else:
                if root_x < root_y:
                    parent[root_y] = root_x
                else:
                    parent[root_x] = root_y

    parties = []
    for _ in range(m):
        party_info = list(map(int, input().split()))
        attendees = party_info[1:]
        parties.append(attendees)
        
        if len(attendees) > 1:
            first_person = attendees[0]
            for i in range(1, len(attendees)):
                union(first_person, attendees[i])

    updated_truth_knowers = set()
    for person in truth_knowers:
        updated_truth_knowers.add(find(person))
    truth_knowers = updated_truth_knowers

    lie_party_cnt = 0
    for party in parties:
        can_lie = True
        for person in party:
            if find(person) in truth_knowers:
                can_lie = False
                break
        if can_lie:
            lie_party_cnt += 1
    
    answer = lie_party_cnt
    return answer

if __name__ == "__main__":
    n, m = map(int, input().split())
    print(solution(n, m))