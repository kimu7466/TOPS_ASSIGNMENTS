#include <iostream>
#include <string>
using namespace std;

class Cricketer {
protected:
    string name;
    int age;

public:
    
    void inputData() {
        cout << "Enter Cricketer's Name: ";
        cin.ignore(); 
        getline(cin, name);
        cout << "Enter Cricketer's Age: ";
        cin >> age;
    }
};


class Batsman : public Cricketer {
private:
    int totalRuns;
    double averageRuns;
    int bestPerformance;

public:
    
    void inputBatsmanData() {
        cout << "Enter Total Runs Scored: ";
        cin >> totalRuns;
        cout << "Enter Average Runs: ";
        cin >> averageRuns;
        cout << "Enter Best Performance (in a single innings): ";
        cin >> bestPerformance;
    }

    
    void calculateAverage() {
        averageRuns = static_cast<double>(totalRuns) / 50; 
    }

    
    void displayData() {
        cout << "\nCricketer's Information" << endl;
        cout << "Name: " << name << endl;
        cout << "Age: " << age << " years" << endl;

        cout << "\nBatsman's Information" << endl;
        cout << "Total Runs Scored: " << totalRuns << endl;
        cout << "Average Runs per Match: " << averageRuns << endl;
        cout << "Best Performance in an Innings: " << bestPerformance << endl;
    }
};

int main() {
    Batsman batsman;

    
    batsman.inputData();

    
    batsman.inputBatsmanData();

    
    batsman.calculateAverage();

    
    batsman.displayData();

    return 0;
}

