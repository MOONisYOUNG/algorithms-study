#include <stdio.h>

int solution(int n, int s) {
    return s / (n + 1);
}

int main() {
    int n, s;
    while (scanf("%d %d", &n, &s) != EOF) {
        printf("%d\n", solution(n, s));
    }
    return 0;
}