#include<iostream>

class SwapNumbers {
private:
    int num1;
    int num2;

public:
    SwapNumbers(int a, int b) {
        num1 = a;
        num2 = b;
    }

    friend void swap(SwapNumbers &s);

    void display() {
        std::cout << "After swapping: num1 = " << num1 << ", num2 = " << num2 << std::endl;
    }
};

// Friend function to swap num1 and num2 without using a third variable
void swap(SwapNumbers &s) {
    s.num1 = s.num1 + s.num2;
    s.num2 = s.num1 - s.num2;
    s.num1 = s.num1 - s.num2;
}

int main() {
    int num1, num2;
    std::cout << "Enter two numbers: ";
    std::cin >> num1 >> num2;

    SwapNumbers s(num1, num2);

    std::cout << "Before swapping: num1 = " << num1 << ", num2 = " << num2 << std::endl;

    // Calling the friend function to swap numbers
    swap(s);

    s.display();

    return 0;
}

