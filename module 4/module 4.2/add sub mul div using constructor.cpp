#include <iostream>

class Calculator {
public:
    // Constructor to initialize the operands
    Calculator(double a, double b) {
        operand1 = a;
        operand2 = b;
    }

    // Addition method
    double add() {
        return operand1 + operand2;
    }

    // Subtraction method
    double subtract() {
        return operand1 - operand2;
    }

    // Division method
    double divide() {
        if (operand2 != 0) {
            return operand1 / operand2;
        } else {
            std::cout << "Error: Division by zero is not allowed." << std::endl;
            return 0;
        }
    }

    // Multiplication method
    double multiply() {
        return operand1 * operand2;
    }

private:
    double operand1;
    double operand2;
};

int main() {
    double num1, num2;

    // Input from the user
    std::cout << "Enter the first number: ";
    std::cin >> num1;
    std::cout << "Enter the second number: ";
    std::cin >> num2;

    // Create a Calculator object with the entered numbers
    Calculator calc(num1, num2);

    // Perform addition, subtraction, division, and multiplication
    double additionResult = calc.add();
    double subtractionResult = calc.subtract();
    double divisionResult = calc.divide();
    double multiplicationResult = calc.multiply();

    // Display the results
    std::cout << "Addition result: " << additionResult << std::endl;
    std::cout << "Subtraction result: " << subtractionResult << std::endl;
    std::cout << "Division result: " << divisionResult << std::endl;
    std::cout << "Multiplication result: " << multiplicationResult << std::endl;

    return 0;
}

