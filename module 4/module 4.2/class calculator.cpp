#include <iostream>

class Calculator {
public:
    // Constructor
    Calculator() {
        result = 0.0;
    }

    // Addition method
    double add(double a, double b) {
        result = a + b;
        return result;
    }

    // Subtraction method
    double subtract(double a, double b) {
        result = a - b;
        return result;
    }

    // Multiplication method
    double multiply(double a, double b) {
        result = a * b;
        return result;
    }

    // Division method
    double divide(double a, double b) {
        if (b != 0) {
            result = a / b;
        } else {
            std::cout << "Error: Division by zero is not allowed." << std::endl;
        }
        return result;
    }

    // Get the current result
    double getResult() {
        return result;
    }

private:
    double result;
};

int main() {
    Calculator calc;

    double num1, num2;
    char operation;

    std::cout << "Simple Calculator" << std::endl;
    std::cout << "Enter first number: ";
    std::cin >> num1;

    std::cout << "Enter operation (+, -, *, /): ";
    std::cin >> operation;

    std::cout << "Enter second number: ";
    std::cin >> num2;

    switch (operation) {
        case '+':
            calc.add(num1, num2);
            break;
        case '-':
            calc.subtract(num1, num2);
            break;
        case '*':
            calc.multiply(num1, num2);
            break;
        case '/':
            calc.divide(num1, num2);
            break;
        default:
            std::cout << "Invalid operation!" << std::endl;
            return 1;
    }

    std::cout << "Result: " << calc.getResult() << std::endl;

    return 0;
}

