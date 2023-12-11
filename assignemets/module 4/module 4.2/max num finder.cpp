#include<iostream>

class MaxNumberFinder {
private:
    int num1;
    int num2;

public:
    MaxNumberFinder(int a, int b) {
        num1 = a;
        num2 = b;
    }

    friend int findMax(MaxNumberFinder &m);
};

// Friend function to find the maximum of num1 and num2
int findMax(MaxNumberFinder &m) {
    if (m.num1 > m.num2) {
        return m.num1;
    } else {
        return m.num2;
    }
}

int main() {
    int num1, num2;
    std::cout << "Enter two numbers: ";
    std::cin >> num1 >> num2;

    MaxNumberFinder m(num1, num2);

    int max = findMax(m);

    std::cout << "The maximum number is: " << max << std::endl;

    return 0;
}

