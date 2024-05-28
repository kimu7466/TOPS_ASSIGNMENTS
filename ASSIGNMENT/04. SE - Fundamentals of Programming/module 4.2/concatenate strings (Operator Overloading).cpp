#include <iostream>
#include <string>
using namespace std;

class Concatenator {
private:
    string str;

public:
    Concatenator(const string& s) : str(s) {}

    Concatenator operator+(const Concatenator& other) const {
        return Concatenator(this->str + other.str);
    }

    string getResult() const {
        return str;
    }
};

int main() {
    string str1, str2;
    cout << "Enter the first string: ";
    getline(cin, str1);
    cout << "Enter the second string: ";
    getline(cin, str2);

    Concatenator concat1(str1);
    Concatenator concat2(str2);

    Concatenator result = concat1 + concat2;

    cout << "Concatenated String: " << result.getResult() << endl;

    return 0;
}

