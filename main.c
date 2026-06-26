#include<iostream>
int main() {
    int n;
    std::cout << "Enter a number: ";
    std::cin >> n;
    int fact = 1;
    for(int i = 1; i <= n; ++i) {
        fact *= i;
    }
    std::cout << "Factorial of " << n << " is " << fact << std::endl;
    return 0;
}