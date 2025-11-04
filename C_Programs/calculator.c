#include <stdio.h>

int main(void) {
    double a, b;
    char op;
    printf("Enter expression (e.g. 2.5 + 3): ");
    if (scanf("%lf %c %lf", &a, &op, &b) != 3) {
        fprintf(stderr, "Invalid input\n");
        return 1;
    }
    double r;
    int ok = 1;
    switch (op) {
        case '+': r = a + b; break;
        case '-': r = a - b; break;
        case '*': r = a * b; break;
        case '/': if (b == 0) { fprintf(stderr, "Division by zero\n"); return 1; } r = a / b; break;
        default: ok = 0;
    }
    if (!ok) { fprintf(stderr, "Unsupported operator: %c\n", op); return 1; }
    printf("Result: %g\n", r);
    return 0;
}
