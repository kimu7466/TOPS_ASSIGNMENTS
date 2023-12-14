#include <iostream>

// Inline function to calculate multiplication
inline double multiply(double x, double y) {
    return x * y;
}

// Inline function to calculate the cubic value
inline double cube(double x) {
    return x * x * x;
}

int main() {
    double num;
    
    // Input from the user
    std::cout << "Enter a number: ";
    std::cin >> num;

    // Calculate multiplication value using the inline function
    double multiplicationResult = multiply(num, 5.0);

    // Calculate cubic value using the inline function
    double cubicResult = cube(num);

    // Display the results
    std::cout << "Multiplication result: " << multiplicationResult << std::endl;
    std::cout << "Cubic result: " << cubicResult << std::endl;

    return 0;
}

