#include <iostream>

unsigned long long factorial(unsigned int n) {
    unsigned long long res = 1;
    for (unsigned int i = 2; i <= n; ++i) res *= i;
    return res;
}

int main() {
    unsigned int n = 10;
    std::cout << "factorial(" << n << ") = " << factorial(n) << std::endl;
    return 0;
}
