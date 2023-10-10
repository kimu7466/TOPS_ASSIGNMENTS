#include <iostream>
#include <string>

// Base class Cricketer
class Cricketer {
protected:
    std::string name;
    int age;

public:
    // Member function to input data for a cricketer
    void inputData() {
        std::cout << "Enter Cricketer's Name: ";
        std::cin.ignore(); // Clear any previous newline character
        std::getline(std::cin, name);
        std::cout << "Enter Cricketer's Age: ";
        std::cin >> age;
    }
};

// Derived class Batsman
class Batsman : public Cricketer {
private:
    int totalRuns;
    double averageRuns;
    int bestPerformance;

public:
    // Member function to input additional data for a batsman
    void inputBatsmanData() {
        std::cout << "Enter Total Runs Scored: ";
        std::cin >> totalRuns;
        std::cout << "Enter Average Runs: ";
        std::cin >> averageRuns;
        std::cout << "Enter Best Performance (in a single innings): ";
        std::cin >> bestPerformance;
    }

    // Member function to calculate average runs
    void calculateAverage() {
        averageRuns = static_cast<double>(totalRuns) / 50; // Assuming 50 matches for simplicity
    }

    // Member function to display cricketer and batsman data
    void displayData() {
        std::cout << "\nCricketer's Information" << std::endl;
        std::cout << "Name: " << name << std::endl;
        std::cout << "Age: " << age << " years" << std::endl;

        std::cout << "\nBatsman's Information" << std::endl;
        std::cout << "Total Runs Scored: " << totalRuns << std::endl;
        std::cout << "Average Runs per Match: " << averageRuns << std::endl;
        std::cout << "Best Performance in an Innings: " << bestPerformance << std::endl;
    }
};

int main() {
    Batsman batsman;

    // Input data for the cricketer
    batsman.inputData();

    // Input data specific to the batsman
    batsman.inputBatsmanData();

    // Calculate average runs
    batsman.calculateAverage();

    // Display cricketer and batsman data
    batsman.displayData();

    return 0;
}

