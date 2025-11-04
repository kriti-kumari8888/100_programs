#include <iostream>

int main() {
    double a = 12.5, b = 3.0;
    std::cout << "a = " << a << ", b = " << b << "\n";
    std::cout << "a + b = " << (a + b) << "\n";
    std::cout << "a - b = " << (a - b) << "\n";
    std::cout << "a * b = " << (a * b) << "\n";
    if (b != 0) std::cout << "a / b = " << (a / b) << "\n";
    return 0;
}
