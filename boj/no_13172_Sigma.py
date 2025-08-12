import sys
input = sys.stdin.readline

MOD = 1000000007

def power(base: int, exp: int) -> int:
    res = 1
    base %= MOD
    while exp > 0:
        if exp % 2 == 1:
            res = (res * base) % MOD
        base = (base * base) % MOD
        exp //= 2
    return res

def mod_inverse(n: int) -> int:
    return power(n, MOD - 2)

def solution(m: int) -> int:
    total_expected_value = 0

    for _ in range(m):
        n, s = map(int, input().split())
        
        s_mod = s % MOD
        n_inverse = mod_inverse(n)

        current_die_expected_value = (s_mod * n_inverse) % MOD
        total_expected_value = (total_expected_value + current_die_expected_value) % MOD

    answer = total_expected_value
    return answer

if __name__ == "__main__":
    m = int(input())
    print(solution(m))