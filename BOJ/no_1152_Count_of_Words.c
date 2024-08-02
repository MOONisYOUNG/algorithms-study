#include <stdio.h>
#include <string.h>

int main() {
    char input[1000001];
    char *token;
    int count = 0;

    fgets(input, sizeof(input), stdin);

    token = strtok(input, " \t\n");
    while (token != NULL) {
        count++;
        token = strtok(NULL, " \t\n");
    }

    printf("%d\n", count);
    
    return 0;
}