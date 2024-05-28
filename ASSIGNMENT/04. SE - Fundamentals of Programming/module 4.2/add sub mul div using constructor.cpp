#include <iostream>
using namespace std;

class Calculator {
    public:
        Calculator(double a, double b) {
            operand1 = a;
            operand2 = b;
        }
        
        double add() {
            return operand1 + operand2;
        }

        double subtract() {
            return operand1 - operand2;
        }
        
        double divide() {
            if (operand2 != 0) {
                return operand1 / operand2;
            } else {
                cout << "Error: Division by zero is not allowed." << endl;
                return 0;
            }
        }
        
        double multiply() {
            return operand1 * operand2;
        }

    private:
        double operand1;
        double operand2;
};

int main() {
    double num1, num2;
    
    cout << "Enter the first number: ";
    cin >> num1;
    cout << "Enter the second number: ";
    cin >> num2;

    Calculator calc(num1, num2);

    double additionResult = calc.add();
    double subtractionResult = calc.subtract();
    double divisionResult = calc.divide();
    double multiplicationResult = calc.multiply();

    cout << "Addition result: " << additionResult << endl;
    cout << "Subtraction result: " << subtractionResult << endl;
    cout << "Division result: " << divisionResult << endl;
    cout << "Multiplication result: " << multiplicationResult << endl;

    return 0;
}

