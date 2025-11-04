#include <iostream>
#include <array>

int main() {
    std::array<std::array<int,2>,2> A = {{{1,2},{3,4}}};
    std::array<std::array<int,2>,2> B = {{{5,6},{7,8}}};
    std::array<std::array<int,2>,2> C = {{{0,0},{0,0}}};
    for (int i=0;i<2;++i)
        for (int j=0;j<2;++j)
            for (int k=0;k<2;++k)
                C[i][j] += A[i][k]*B[k][j];
    std::cout << "Product matrix:\n";
    for (int i=0;i<2;++i) {
        for (int j=0;j<2;++j) std::cout << C[i][j] << " ";
        std::cout << '\n';
    }
    return 0;
}
