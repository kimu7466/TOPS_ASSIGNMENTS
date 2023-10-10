#include <iostream>
#include <string>

class Concatenator {
private:
    std::string str;

public:
    // Constructor to initialize the Concatenator with a string
    Concatenator(const std::string& s) : str(s) {}

    // Overload the '+' operator for string concatenation
    Concatenator operator+(const Concatenator& other) const {
        return Concatenator(this->str + other.str);
    }

    // Member function to get the concatenated string
    std::string getResult() const {
        return str;
    }
};

int main() {
    // Input two strings
    std::string str1, str2;
    std::cout << "Enter the first string: ";
    std::getline(std::cin, str1);
    std::cout << "Enter the second string: ";
    std::getline(std::cin, str2);

    // Create Concatenator objects from the input strings
    Concatenator concat1(str1);
    Concatenator concat2(str2);

    // Perform string concatenation using operator overloading
    Concatenator result = concat1 + concat2;

    // Display the concatenated string
    std::cout << "Concatenated String: " << result.getResult() << std::endl;

    return 0;
}

