#include <stdio.h>
#include <stdint.h>

unsigned long long factorial(unsigned int n) {
    unsigned long long r = 1;
    for (unsigned int i = 2; i <= n; ++i) r *= i;
    return r;
}

int main(void) {
    unsigned int n;
    printf("Enter a non-negative integer: ");
    if (scanf("%u", &n) != 1) {
        fprintf(stderr, "Invalid input\n");
        return 1;
    }
    printf("%u! = %llu\n", n, factorial(n));
    return 0;
}
