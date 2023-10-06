#include <iostream>
using namespace std;

class Calculator {
public:
    double add(double x, double y) {
        return x + y;
    }

    double subtract(double x, double y) {
        return x - y;
    }

    double multiply(double x, double y) {
        return x * y;
    }

    double divide(double x, double y) {
        if (y == 0) {
            cout << "Cannot divide by zero" << endl;
            return 0.0;
        }
        return x / y;
    }
};

int main() {
    Calculator calc;
    char operation;

    while (true) {
        cout << "Options:" << endl;
        cout << "Enter '+' for addition" << endl;
        cout << "Enter '-' for subtraction" << endl;
        cout << "Enter '*' for multiplication" << endl;
        cout << "Enter '/' for division" << endl;
        cout << "Enter 'q' to quit" << endl;

        cin >> operation;

        if (operation == 'q') {
            break;
        } else if (operation == '+' || operation == '-' || operation == '*' || operation == '/') {
            double num1, num2;
            cout << "Enter first number: ";
            cin >> num1;
            cout << "Enter second number: ";
            cin >> num2;

            switch (operation) {
                case '+':
                    cout << "Result: " << calc.add(num1, num2) << endl;
                    break;
                case '-':
                    cout << "Result: " << calc.subtract(num1, num2) << endl;
                    break;
                case '*':
                    cout << "Result: " << calc.multiply(num1, num2) << endl;
                    break;
                case '/':
                    cout << "Result: " << calc.divide(num1, num2) << endl;
                    break;
            }
        } else {
            cout << "Invalid input. Please try again." << endl;
        }
    }

    return 0;
}

