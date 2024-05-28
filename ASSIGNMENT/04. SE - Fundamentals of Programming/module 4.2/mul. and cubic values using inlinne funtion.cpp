#include <iostream>
using namespace std;

inline double multiply(double x, double y) {
    return x * y;
}

inline double cube(double x) {
    return x * x * x;
}

int main() {
    double num;
    
    cout << "Enter a number: ";
    cin >> num;

    double multiplicationResult = multiply(num, 5.0);

    double cubicResult = cube(num);

    cout << "Multiplication result: " << multiplicationResult << endl;
    cout << "Cubic result: " << cubicResult << endl;

    return 0;
}

