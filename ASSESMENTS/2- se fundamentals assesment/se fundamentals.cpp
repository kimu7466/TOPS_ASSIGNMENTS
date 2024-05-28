#include <iostream>
#include <string>

using namespace std;

string reverseString(const string& inputString) {
    return string(inputString.rbegin(), inputString.rend());
}

bool isPalindrome(const string& inputString) {
    string reversedString = reverseString(inputString);
    return inputString == reversedString;
}

int characterFrequency(const string& inputString, char ch) {
    int count = 0;
    for (char c : inputString) {
        if (c == ch)
            count++;
    }
    return count;
}

pair<int, int> countVowelsConsonants(const string& inputString) {
    int vowels = 0, consonants = 0;
    for (char c : inputString) {
        if (isalpha(c)) {
            if (tolower(c) == 'a' || tolower(c) == 'e' || tolower(c) == 'i' || tolower(c) == 'o' || tolower(c) == 'u')
                vowels++;
            else
                consonants++;
        }
    }
    return make_pair(vowels, consonants);
}

void displayMenu() {
    cout << "\n         String Operations Menu:" << endl;
    cout << "       1. Reverse a string" << endl;
    cout << "       2. Palindrome check" << endl;
    cout << "       3. Frequency of a character in a string" << endl;
    cout << "       4. Count number of vowels and consonants" << endl;
    cout << "       0. Exit" << endl;
}

int main() {
    while (true) {
        displayMenu();
        char choice;
        cout << "Enter your choice (0-4): ";
        cin >> choice;

        if (choice == '1') {
            string inputStr;
            cout << "Enter a string: ";
            cin.ignore(); 
            getline(cin, inputStr);
            cout << "Reversed string: " << reverseString(inputStr) << endl;
        }

        else if (choice == '2') {
            string inputStr;
            cout << "Enter a string: ";
            cin.ignore(); 
            getline(cin, inputStr);
            if (isPalindrome(inputStr))
                cout << "The string is a palindrome." << endl;
            else
                cout << "The string is not a palindrome." << endl;
        }

        else if (choice == '3') {
            string inputStr;
            char character;
            cout << "Enter a string: ";
            cin.ignore(); 
            getline(cin, inputStr);
            cout << "Enter a character: ";
            cin >> character;
            cout << "Frequency of '" << character << "' in the string: "
                 << characterFrequency(inputStr, character) << endl;
        }

        else if (choice == '4') {
            string inputStr;
            cout << "Enter a string: ";
            cin.ignore(); 
            getline(cin, inputStr);
            pair<int, int> counts = countVowelsConsonants(inputStr);
            cout << "Number of vowels: " << counts.first << endl;
            cout << "Number of consonants: " << counts.second << endl;
        }

        else if (choice == '0') {
            cout << "Exiting the program. Goodbye!" << endl;
            break;
        }

        else {
            cout << "Invalid choice! Please enter a valid option." << endl;
        }

        char continueChoice;
        cout << "Do you want to continue (y/n)? ";
        cin >> continueChoice;
        if (tolower(continueChoice) != 'y') {
            cout << "Exiting the program. Goodbye!" << endl;
            break;
        }
    }

    return 0;
}

