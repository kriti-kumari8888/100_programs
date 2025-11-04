#include <iostream>
#include <fstream>

int main() {
    const char* src = "C:/100_Programs/hello.txt";
    const char* dst = "C:/100_Programs/copied_hello.txt";
    std::ifstream in(src, std::ios::binary);
    if (!in) {
        std::cerr << "Cannot open source file: " << src << '\n';
        return 1;
    }
    std::ofstream out(dst, std::ios::binary);
    out << in.rdbuf();
    std::cout << "Copied " << src << " -> " << dst << '\n';
    return 0;
}
