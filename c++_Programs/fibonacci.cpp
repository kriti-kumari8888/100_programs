#include <iostream>
#include <vector>

int main() {
    int n = 10;
    std::vector<unsigned long long> f(n);
    if (n > 0) f[0] = 0;
    if (n > 1) f[1] = 1;
    for (int i = 2; i < n; ++i) f[i] = f[i-1] + f[i-2];
    std::cout << "First " << n << " Fibonacci numbers:\n";
    for (auto val : f) std::cout << val << " ";
    std::cout << std::endl;
    return 0;
}
