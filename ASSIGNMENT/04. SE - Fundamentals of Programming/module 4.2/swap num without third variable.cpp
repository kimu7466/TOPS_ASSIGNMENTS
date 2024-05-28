#include<iostream>
using namespace std;

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
        cout << "After swapping: num1 = " << num1 << ", num2 = " << num2 << endl;
    }
};

void swap(SwapNumbers &s) {
    s.num1 = s.num1 + s.num2;
    s.num2 = s.num1 - s.num2;
    s.num1 = s.num1 - s.num2;
}

int main() {
    int num1, num2;
    cout << "Enter two numbers: ";
    cin >> num1 >> num2;

    SwapNumbers s(num1, num2);

    cout << "Before swapping: num1 = " << num1 << ", num2 = " << num2 << endl;

    swap(s);

    s.display();

    return 0;
}

