#include <stdio.h>

int main(void) {
    int n;
    printf("Enter N (>=1): ");
    if (scanf("%d", &n) != 1 || n < 1) {
        fprintf(stderr, "Invalid input\n");
        return 1;
    }
    long long a = 0, b = 1;
    printf("Fibonacci:");
    for (int i = 0; i < n; ++i) {
        printf(" %lld", a);
        long long t = a + b;
        a = b;
        b = t;
    }
    printf("\n");
    return 0;
}
