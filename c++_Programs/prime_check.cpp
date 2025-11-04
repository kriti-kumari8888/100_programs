#include <iostream>
#include <cmath>

bool is_prime(int n) {
    if (n <= 1) return false;
    if (n <= 3) return true;
    if (n % 2 == 0) return false;
    int r = static_cast<int>(std::sqrt(n));
    for (int i = 3; i <= r; i += 2)
        if (n % i == 0) return false;
    return true;
}

int main() {
    int n = 97;
    std::cout << n << (is_prime(n) ? " is prime\n" : " is not prime\n");
    return 0;
}
