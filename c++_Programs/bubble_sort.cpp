#include <iostream>
#include <vector>

void bubble_sort(std::vector<int>& a) {
    bool swapped;
    for (size_t i = 0; i < a.size(); ++i) {
        swapped = false;
        for (size_t j = 1; j + i < a.size(); ++j) {
            if (a[j-1] > a[j]) {
                std::swap(a[j-1], a[j]);
                swapped = true;
            }
        }
        if (!swapped) break;
    }
}

int main() {
    std::vector<int> v = {5, 2, 9, 1, 5, 6};
    bubble_sort(v);
    for (int x : v) std::cout << x << " ";
    std::cout << std::endl;
    return 0;
}
