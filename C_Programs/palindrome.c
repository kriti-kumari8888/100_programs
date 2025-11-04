#include <stdio.h>
#include <string.h>

int main(void) {
    char s[1024];
    printf("Enter a string: ");
    if (!fgets(s, sizeof(s), stdin)) return 1;
    size_t len = strcspn(s, "\n");
    s[len] = '\0';
    size_t i = 0, j = len ? len - 1 : 0;
    int ok = 1;
    while (i < j) {
        if (s[i] != s[j]) { ok = 0; break; }
        ++i; --j;
    }
    printf("The string \"%s\" is %s palindrome\n", s, ok ? "a" : "not a");
    return 0;
}
