#include <iostream>
#include <cmath>

const double PI = 3.14159265359;

// Function to calculate the area of a circle
double calculateArea(double radius) {
    return PI * radius * radius;
}

// Function to calculate the area of a rectangle
double calculateArea(double length, double width) {
    return length * width;
}

// Function to calculate the area of a triangle
double calculateArea(double base, double height, char shape) {
    if (shape == 't' || shape == 'T') {
        return 0.5 * base * height;
    } else {
        std::cerr << "Invalid shape character. Use 't' or 'T' for triangle." << std::endl;
        return 0.0;
    }
}

int main() {
    char choice;
    std::cout << "Choose a shape to calculate area (C for circle, R for rectangle, T for triangle): ";
    std::cin >> choice;

    if (choice == 'C' || choice == 'c') {
        double radius;
        std::cout << "Enter the radius of the circle: ";
        std::cin >> radius;
        std::cout << "Area of the circle: " << calculateArea(radius) << std::endl;
    } else if (choice == 'R' || choice == 'r') {
        double length, width;
        std::cout << "Enter the length and width of the rectangle: ";
        std::cin >> length >> width;
        std::cout << "Area of the rectangle: " << calculateArea(length, width) << std::endl;
    } else if (choice == 'T' || choice == 't') {
        double base, height;
        std::cout << "Enter the base and height of the triangle: ";
        std::cin >> base >> height;
        std::cout << "Area of the triangle: " << calculateArea(base, height, 't') << std::endl;
    } else {
        std::cerr << "Invalid choice. Use 'C', 'R', or 'T'." << std::endl;
    }

    return 0;
}

