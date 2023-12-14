#include <iostream>

// Function to perform addition
double calculate(double a, double b) {
    return a + b;
}

// Function to perform subtraction
double calculate(int a, int b) {
    return a - b;
}

// Function to perform multiplication
double calculate(double a, int b) {
    return a * b;
}

// Function to perform division
double calculate(int a, double b) {
    if (b != 0.0) {
        return a / b;
    } else {
        std::cout << "Error: Division by zero is not allowed." << std::endl;
        return 0.0;
    }
}

int main() {
    double num1, num2;

    // Input two numbers
    std::cout << "Enter the first number: ";
    std::cin >> num1;
    std::cout << "Enter the second number: ";
    std::cin >> num2;

    // Perform addition, subtraction, multiplication, and division
    double additionResult = calculate(num1, num2);
    double subtractionResult = calculate(static_cast<int>(num1), static_cast<int>(num2));
    double multiplicationResult = calculate(num1, static_cast<int>(num2));
    double divisionResult = calculate(static_cast<int>(num1), num2);

    // Display results
    std::cout << "Addition result: " << additionResult << std::endl;
    std::cout << "Subtraction result: " << subtractionResult << std::endl;
    std::cout << "Multiplication result: " << multiplicationResult << std::endl;
    std::cout << "Division result: " << divisionResult << std::endl;

    return 0;
}

