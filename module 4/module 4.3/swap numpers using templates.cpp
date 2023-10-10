#include <iostream>

// Template function to swap two values of any data type
template <typename T>
void swapValues(T &a, T &b) {
    T temp = a;
    a = b;
    b = temp;
}

int main() {
    int num1, num2;
    std::cout << "Enter two integer values: ";
    std::cin >> num1 >> num2;

    std::cout << "Before swapping: num1 = " << num1 << ", num2 = " << num2 << std::endl;

    // Swap two integer values using the template function
    swapValues(num1, num2);

    std::cout << "After swapping: num1 = " << num1 << ", num2 = " << num2 << std::endl;

    double dbl1, dbl2;
    std::cout << "Enter two double values: ";
    std::cin >> dbl1 >> dbl2;

    std::cout << "Before swapping: dbl1 = " << dbl1 << ", dbl2 = " << dbl2 << std::endl;

    // Swap two double values using the same template function
    swapValues(dbl1, dbl2);

    std::cout << "After swapping: dbl1 = " << dbl1 << ", dbl2 = " << dbl2 << std::endl;

    return 0;
}

