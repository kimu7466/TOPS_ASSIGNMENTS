#include <iostream>
#include <cmath>
using namespace std;

const double PI = 3.14159265359;

double calculateArea(double radius) {
    return PI * radius * radius;
}

double calculateArea(double length, double width) {
    return length * width;
}

double calculateArea(double base, double height, char shape) {
    if (shape == 't' || shape == 'T') {
        return 0.5 * base * height;
    } else {
        cerr << "Invalid shape character. Use 't' or 'T' for triangle." << endl;
        return 0.0;
    }
}

int main() {
    char choice;
    cout << "Choose a shape to calculate area (C for circle, R for rectangle, T for triangle): ";
    cin >> choice;

    if (choice == 'C' || choice == 'c') {
        double radius;
        cout << "Enter the radius of the circle: ";
        cin >> radius;
        cout << "Area of the circle: " << calculateArea(radius) << endl;
    } else if (choice == 'R' || choice == 'r') {
        double length, width;
        cout << "Enter the length and width of the rectangle: ";
        cin >> length >> width;
        cout << "Area of the rectangle: " << calculateArea(length, width) << endl;
    } else if (choice == 'T' || choice == 't') {
        double base, height;
        cout << "Enter the base and height of the triangle: ";
        cin >> base >> height;
        cout << "Area of the triangle: " << calculateArea(base, height, 't') << endl;
    } else {
        cerr << "Invalid choice. Use 'C', 'R', or 'T'." << endl;
    }

    return 0;
}

