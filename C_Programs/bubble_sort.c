#include <stdio.h>

void bubble_sort(int *a, int n) {
    for (int i = 0; i < n - 1; ++i)
        for (int j = 0; j < n - 1 - i; ++j)
            if (a[j] > a[j + 1]) {
                int t = a[j];
                a[j] = a[j + 1];
                a[j + 1] = t;
            }
}

int main(void) {
    int a[] = {64, 34, 25, 12, 22, 11, 90};
    int n = sizeof(a) / sizeof(a[0]);
    printf("Before:");
    for (int i = 0; i < n; ++i) printf(" %d", a[i]);
    printf("\n");

    bubble_sort(a, n);

    printf("After:");
    for (int i = 0; i < n; ++i) printf(" %d", a[i]);
    printf("\n");
    return 0;
}
