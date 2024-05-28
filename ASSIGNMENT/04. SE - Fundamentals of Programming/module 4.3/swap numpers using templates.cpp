#include <iostream>
using namespace std;

template <typename T>
void swapValues(T &a, T &b) {
    T temp = a;
    a = b;
    b = temp;
}

int main() {
    int num1, num2;
    cout << "Enter two integer values: ";
    cin >> num1 >> num2;

    cout << "Before swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
    
    swapValues(num1, num2);

    cout << "After swapping: num1 = " << num1 << ", num2 = " << num2 << endl;

    double dbl1, dbl2;
    cout << "Enter two double values: ";
    cin >> dbl1 >> dbl2;

    cout << "Before swapping: dbl1 = " << dbl1 << ", dbl2 = " << dbl2 << endl;
    
    swapValues(dbl1, dbl2);

    cout << "After swapping: dbl1 = " << dbl1 << ", dbl2 = " << dbl2 << endl;

    return 0;
}

