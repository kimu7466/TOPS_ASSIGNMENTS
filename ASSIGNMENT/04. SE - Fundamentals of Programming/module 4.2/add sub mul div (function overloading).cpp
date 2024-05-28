#include <iostream>
using namespace std;

double calculate(double a, double b) {
    return a + b;
}

double calculate(int a, int b) {
    return a - b;
}

double calculate(double a, int b) {
    return a * b;
}

double calculate(int a, double b) {
    if (b != 0.0) {
        return a / b;
    } else {
        cout << "Error: Division by zero is not allowed." << endl;
        return 0.0;
    }
}

int main() {
    double num1, num2;
    
    cout << "Enter the first number: ";
    cin >> num1;
    cout << "Enter the second number: ";
    cin >> num2;
    
    double additionResult = calculate(num1, num2);
    double subtractionResult = calculate(static_cast<int>(num1), static_cast<int>(num2));
    double multiplicationResult = calculate(num1, static_cast<int>(num2));
    double divisionResult = calculate(static_cast<int>(num1), num2);
    
    cout << "Addition result: " << additionResult << endl;
    cout << "Subtraction result: " << subtractionResult << endl;
    cout << "Multiplication result: " << multiplicationResult << endl;
    cout << "Division result: " << divisionResult << endl;

    return 0;
}

