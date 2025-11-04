#include <iostream>
#include <string>
#include <algorithm>

int main() {
    std::string s = "madam";
    std::string t = s;
    std::reverse(t.begin(), t.end());
    std::cout << s << (s == t ? " is a palindrome\n" : " is not a palindrome\n");
    return 0;
}
